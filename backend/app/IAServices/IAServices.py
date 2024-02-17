class IA:
    def __init__(self):
        print("IA.__init__")
    
    def get_healthy_recipes(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum):
        print("IA.get_healthy_recipes")
        return ("Receta 1", "Receta 2", "Receta 3")
    
    def get_healthy_exercises(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine):
        print("IA.get_healthy_exercises")
        return ("Ejercicio 1", "Ejercicio 2", "Ejercicio 3")