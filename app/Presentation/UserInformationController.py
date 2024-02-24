from app.AppServices.UserInformationServices import UserInformationServices
from flask_restx import Resource, Namespace, fields
from injector import inject
from app.Presentation.DTO.UserInformationDTO import user_information_dto
from app.SparkServices.SparkServices import SparkServices

api = Namespace('userinformation', description='User information related operations')

UserInformation, GetPredictionResponse = user_information_dto(api)

@api.route('/', strict_slashes=False)
class UserInformationController(Resource):
    @inject
    def __init__(self, user_information_services: UserInformationServices, **kwargs):
        self.user_information_services = user_information_services
        super().__init__(**kwargs)

    @api.expect(UserInformation)
    @api.marshal_with(GetPredictionResponse)
    def post(self):
        death_prediction = self.user_information_services.get_prediction(**api.payload)
        print("Predicción Controller: ", death_prediction)
        return {'death_prediction': death_prediction}, 200

    # @api.expect(UserInformation)
    # @api.marshal_with(GetPredictionResponse)
    # def get(self):
    #     return self.user_information_services.get_prediction(**api.payload)


@api.route('/run-analysis', strict_slashes=False)
class RunAnalysis(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, **kwargs):
        self.spark_services = spark_services
        super().__init__(**kwargs)

    def get(self):
        result = self.spark_services.run_analysis()
        return {'result': result}, 200


@api.route('/read-file', strict_slashes=False)
class ReadFile(Resource):
    @inject
    def __init__(self, spark_services: SparkServices, **kwargs):
        self.spark_services = spark_services
        super().__init__(**kwargs)

    def get(self):
        result = self.spark_services.read_file()
        return {'result': result}, 200