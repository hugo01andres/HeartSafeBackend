# Tenemos que importar a la IA para que nos haga la predicción
# from spark import Spark
# from ia import IA

class UserInformationServices:

    def __init__(self):
        print("UserRequest.__init__")
        # self.spark_functions = Spark()
        # self.ia_functions = IA()



    def get_prediction(self, age=None, anaemia=None, creatine_phosphokinase=None, diabetes=None, ejection_fraction=None, high_blood_pressure=None, platelets=None, serum_creatinine=None, serum_sodium=None, sex=None, smoking=None, time=None):
        death_prediction = "10%"
        print("UserRequest.get_information")
        # Imprimir toda la información
        print("Edad: ", age)
        print("Anemia: ", anaemia)
        print("Creatine phosphokinase: ", creatine_phosphokinase)
        print("Diabetes: ", diabetes)
        print("Ejection fraction: ", ejection_fraction)
        print("High blood pressure: ", high_blood_pressure)
        print("Platelets: ", platelets)
        print("Serum creatinine: ", serum_creatinine)
        print("Serum sodium: ", serum_sodium)
        print("sex", sex)
        print("Smoking: ", smoking)
        print("Time: ", time)

        # TODO: Estos datos los tenemos que mandar a una función que se encargue de hacer la predicción
        # death_prediction = self.spark_get_prediction(age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium
        print("Predicción: ", death_prediction)
        return death_prediction
        

    def get_healthy_recipes(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum):
        print("UserRequest.get_healthy_recipes")
        healthy_recipes = self.ia_functions.get_healthy_recipes(age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum)
        return healthy_recipes

    def get_healthy_exercises(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine):
        print("UserRequest.get_healthy_exercises")
        healthy_exercises = self.ia_functions.get_healthy_exercises(age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine)
        return healthy_exercises