from app.AppServices.UserInformationServices import UserInformationServices
from flask_restx import Resource, Namespace, fields
from injector import inject
from app.IAServices.IAServices import IAServices
from app.Presentation.DTO.UserInformationDTO import user_information_dto
from app.SparkServices.SparkServices import SparkServices

api = Namespace('userinformation', description='User information related operations')

UserInformation, GetPredictionResponse = user_information_dto(api)



""" Este controlador es el que se encarga de hacer la predicción de la muerte del paciente """
@api.route('/', strict_slashes=False)
class PostInformation(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, ia_services: IAServices, **kwargs):
        self.spark_services = spark_services
        self.ia_services = ia_services
        super().__init__(**kwargs)

    # Obtenemos la prediccion
    @api.expect(UserInformation)    
    @api.marshal_with(GetPredictionResponse)
    def post(self):
        """
        Este endpoint recibe la información del usuario y la persiste en el .csv

        Parametros:
           Revisar el UserInformationDTO en especial UserInformation
        """
        self.spark_services.persist_data(api.payload)

        return 200



"""Este controlador se encarga de obtener la información de las graficas y las recetas saludables y ejercicios saludables"""
@api.route('/analysispdf', strict_slashes=False)
class AnalysisPDF(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, ia_services: IAServices, **kwargs):
        self.spark_services = spark_services
        self.ia_services = ia_services
        super().__init__(**kwargs)

        # Obtenemos un pdf con la información
    @api.expect(UserInformation)    
    def post(self):
        """
        Generar un PDF con la información de las graficas y las recetas saludables y ejercicios saludables

        Este endpoint recibe la información de un paciente y devuelve un PDF 
        con la información de las graficas y las recetas saludables y ejercicios 
        saludables

        Parametros:
              Revisar el UserInformationDTO en especial UserInformation
        
        Devuelve:
            - pdf: El PDF con la información de las graficas y las recetas saludables y ejercicios saludables

        Ejemplo:
            {
                "pdf": "JVBERi0xLjQKJZOMi54gUmVwb3J0TGFiIEdlbmVyYXRlZCBQREYgZG9jdW1lbnQgaHR0cDovL3d3dy5yZXBvcnRsYWIuY29tCjEgMCBvYmoKPDwKL0YxIDIgMCBSIC9GMiAzIDAgUgo+PgplbmRvYmoKMiAwIG9iago8PAovQmF"
            }
        """
        data = api.payload.copy()
        
        if data['share_data']:
            self.spark_services.persist_data(data)

        del api.payload['share_data']        

        json_graficas_y_descripciones = self.spark_services.get_graficas_y_descripciones() #Imagenes
        healthy_recipes = self.ia_services.get_healthy_recipes(**api.payload) # TODO: Hugo la esta haciendo
        healthy_exercises = self.ia_services.get_healthy_exercises(**api.payload) # TODO: Hugo la esta haciendo
        pdf = self.ia_services.make_pdf(json_graficas_y_descripciones, healthy_recipes, healthy_exercises) # TODO: Completarla, solamente esta la estructura
        return {'pdf': pdf, 'file_name': 'AnalisisCardiaco.pdf'}, 200
