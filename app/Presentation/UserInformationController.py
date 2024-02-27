from app.AppServices.UserInformationServices import UserInformationServices
from flask_restx import Resource, Namespace, fields
from injector import inject
from app.IAServices.IAServices import IAServices
from app.Presentation.DTO.UserInformationDTO import user_information_dto
from app.SparkServices.SparkServices import SparkServices

api = Namespace('userinformation', description='User information related operations')

UserInformation, GetPredictionResponse = user_information_dto(api)


""" Este controlador puede servir si tenemos que guardar datos o algo, por mientras esta deprecado y no se utilizad """
# @api.route('/', strict_slashes=False)
# class UserInformationController(Resource):
#     @inject
#     def __init__(self, user_information_services: UserInformationServices,spark_services: SparkServices, **kwargs):
#         self.user_information_services = user_information_services
#         self.spark_services = spark_services
#         super().__init__(**kwargs)




""" Este controlador es el que se encarga de hacer la predicción de la muerte del paciente """
@api.route('/analysis', strict_slashes=False)
class RunAnalysis(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, ia_services: IAServices, **kwargs):
        self.spark_services = spark_services
        self.ia_services = ia_services
        super().__init__(**kwargs)

    # Obtenemos la prediccion
    @api.expect(UserInformation)
    @api.marshal_with(GetPredictionResponse)
    def post(self):
        death_prediction = self.spark_services.get_prediction(**api.payload)
        print("Predicción Controller: ", death_prediction)
        # TODO: Retornar death_prediction
        return {'death_prediction': "47%"}, 200

    # Obtenemos un pdf con la información
    @api.expect(UserInformation)
    def get(self):
        graficas = self.spark_services.get_graficas()
        healthy_recipes = self.ia_services.get_healthy_recipes(**api.payload)
        healthy_exercises = self.ia_services.get_healthy_exercises(**api.payload)
        pdf = self.ia_services.make_pdf(graficas, healthy_recipes, healthy_exercises)
        return {'pdf': pdf}, 200



@api.route('/createpdf', strict_slashes=False)
class ReadFile(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, **kwargs):
        self.spark_services = spark_services
        super().__init__(**kwargs)

    def get(self):
        result = self.spark_services.read_file()
        return {'result': result}, 200