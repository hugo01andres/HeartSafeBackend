from flask_restx import Resource, Namespace, fields

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'


def user_information_dto(api):
    UserInformation = api.model('GetUserInfo', {
        'age': fields.Integer(description='Edad', required=False),
        'anaemia': fields.Boolean(description='Anemia', required=False),
        'creatinine_phosphokinase': fields.Integer(description='Creatine phosphokinase', required=False),
        'diabetes': fields.Boolean(description='Diabetes', required=False),
        'ejection_fraction': fields.Integer(description='Ejection fraction', required=False),
        'high_blood_pressure': fields.Boolean(description='High blood pressure', required=False),
        'platelets': fields.Float(description='Platelets', required=False),
        'serum_creatinine': fields.Integer(description='Serum creatinine', required=False),
        'serum_sodium': fields.Float(description='Serum sodium', required=False),
        'sex': fields.Integer(description='sex', required=False),
        'smoking': fields.Boolean(description='Smoking', required=False)
    })
    GetPredictionResponse = api.model('GetPredictionResponse', {
        'death_prediction': fields.String(description='Prediction', required=True)
    })

    return UserInformation, GetPredictionResponse