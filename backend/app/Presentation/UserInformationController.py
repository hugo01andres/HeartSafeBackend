from app.AppServices.UserInformationServices import UserInformationServices
from flask_restx import Resource, Namespace, fields
from injector import inject
from app.Presentation.DTO.UserInformationDTO import user_information_dto

api = Namespace('UserInformation', description='User information related operations')

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