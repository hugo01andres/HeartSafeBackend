from flask_restx import Resource, Namespace, fields

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'


def user_information_dto(api):
    UserInformation = api.model('GetUserInfo', {
        'age': fields.Integer(description='Edad', required=False),
        'anaemia': fields.Integer(description='Anemia', required=False),
        'creatine_phosphokinase': fields.Integer(description='Creatine phosphokinase', required=False),
        'diabetes': fields.Integer(description='Diabetes', required=False),
        'ejection_fraction': fields.Integer(description='Ejection fraction', required=False),
        'high_blood_pressure': fields.Integer(description='High blood pressure', required=False),
        'platelets': fields.Integer(description='Platelets', required=False),
        'serum_creatinine': fields.Integer(description='Serum creatinine', required=False),
        'serum_sodium': fields.Integer(description='Serum sodium', required=False),
        'sex': fields.Integer(description='sex', required=False),
        'smoking': fields.Integer(description='Smoking', required=False),
        'time': fields.Integer(description='Time', required=False)
    })
    GetPredictionResponse = api.model('GetPredictionResponse', {
        'death_prediction': fields.String(description='Prediction', required=True)
    })

    return UserInformation, GetPredictionResponse