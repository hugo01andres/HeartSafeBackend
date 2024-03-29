import os
from pyspark.sql import SparkSession
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import pandas as pd

class SparkServices:
    def __init__(self):
        print("SparkServices initialized")
        self.spark = SparkSession.builder.appName("Flask and Spark: ").master('spark://spark-master:7077').getOrCreate()    

    def get_spark_session(self):
        print("get_spark_session called")

    def persist_data(self, data):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
            df_pandas = df.toPandas()
                    
            data['DEATH_EVENT'] = int(data['death_event'])
            data['time'] = 0

            data.pop('share_data', None)
            data.pop('death_event', None)            

            df_pandas = pd.concat([df_pandas, pd.DataFrame(data, index=[0])], ignore_index=True)
            df_pandas.to_csv('/home/data/heart_failure_clinical_records_dataset.csv', index=False)
        except Exception as e:   
            print(e)

    
    def run_analysis(self):
        print("run_analysis called")
        data = [1, 2, 3, 4, 5]
        distData = self.spark.sparkContext.parallelize(data)
        result = distData.reduce(lambda a, b: a + b)    
        return str(result) + ' is the result of the analysis from Spark!'

    def read_file(self):
        print("read_file called")
        try:
            df = self.spark.read.csv('file:////home/data/starbucks.csv', header=True, inferSchema=True)
            return str(df)
        except Exception as e:   
            print(e)
            return 'File not found!', 404

    
    def probar_test(self):
         print('Probando el servicio de Spark')

    def get_prediction(self, age=None, anaemia=None, creatinine_phosphokinase=None, diabetes=None, ejection_fraction=None, high_blood_pressure=None, platelets=None, serum_creatinine=None, serum=None):
        print("prediccion: ")
        print("get_prediction called")

    def get_graficas_y_descripciones(self):
        """
        Llamo a las funciones que generan las gráficas y las descripciones

        Returns:
            Retorno una lista de jsons con la información de las gráficas y las descripciones
            [{"graficas":"imagen","descripcion":"Lorem ipsum...}]
        """
        json_graficas_y_descripciones = [self.get_grafica_y_descripcion_age(),
                    self.get_grafica_y_descripcion_smooking(),
                    self.get_grafica_y_descripcion_anaemia(),
                    self.get_grafica__y_descripcion_diabetes(),
                    self.get_grafica_y_descripcion_high_blood_pressure()]
        return json_graficas_y_descripciones

      
    def get_grafica_y_descripcion_age(self):
        """
        Generar una gráfica de la edad de los pacientes y una descripción

        Returns:
            Retorna un json con la información de la gráfica y la descripción
            {"graficas":"imagen","descripcion":"Lorem ipsum..."}
        """
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        
        # Generar la gráfica con Plotly Express
        fig = px.box(df, x='sex', y='age', points="all")
        fig.update_layout(
            title_text="Diferencia de edad según el género - Masculino = 1 Femenino =0"
        )       

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/age_distribution_histogram.jpg')

        # Retornar la ruta de la gráfica y una descripción
        get_graficas_age = '/app/app/images/age_distribution_histogram.jpg'
        get_descripcion_age = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

        return {"graficas":get_graficas_age, "descripciones":get_descripcion_age}
    
    def get_grafica_y_descripcion_smooking(self):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        
        # Generar la gráfica con Plotly Express
        fig = px.pie(df, values='smoking',names='DEATH_EVENT', title='Smoking Death Event Ratio')
        fig.update_traces(textposition='inside', textinfo='percent+label') 
        fig.update_layout(
            title_text="Eventos de muerte entre fumadores - Fumador = 1 No fumador = 0"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/smoking_death_event_count.jpg')
        get_graficas_diabetes = '/app/app/images/diabetes_death_event_count.jpg'
        get_descripcion_smooking = "Fumar daña los vasos sanguíneos y aumenta la presión arterial, lo que puede sobrecargar el corazón y aumentar el riesgo de fallo cardiaco. Dejar de fumar es fundamental para mejorar la salud cardiovascular y reducir este riesgo."
        
        return {"graficas":get_graficas_diabetes,"descripciones":get_descripcion_smooking}
    

    def get_grafica_y_descripcion_anaemia(self):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        
        # Generar la gráfica con Plotly Express
        fig = px.pie(df, values='anaemia',names='DEATH_EVENT', title='Anaemia Death Event Ratio')
        fig.update_traces(textposition='inside', textinfo='percent+label') 
        fig.update_layout(
            title_text="Recuento de eventos de muerte por anemia - Anemia = 1 No anemia = 0"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/anaemia_death_event_count.jpg')
        get_graficas_anaemia = '/app/app/images/anaemia_death_event_count.jpg'
        get_descripcion_anaemia = "La anemia puede poner una carga adicional en el corazón al reducir la cantidad de oxígeno que se transporta a los tejidos. Para mejorar la anemia y reducir su impacto en el fallo cardiaco, es importante tratar la causa subyacente, tomar suplementos de hierro si es necesario, considerar transfusiones de sangre en casos graves, seguir una dieta rica en nutrientes y controlar otras condiciones médicas."
        
        return {"graficas":get_graficas_anaemia,"descripciones":get_descripcion_anaemia}
    
    def get_grafica__y_descripcion_diabetes(self):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        
        # Generar la gráfica con Plotly Express
        fig = px.pie(df, values='diabetes',names='DEATH_EVENT', title='Diabetes Death Event Ratio')
        fig.update_traces(textposition='inside', textinfo='percent+label') 
        fig.update_layout(
            title_text="Recuento de eventos de muerte por diabetes - Diabetes = 1 No diabetes = 0"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/diabetes_death_event_count.jpg')
        get_graficas_anaemia = '/app/app/images/anaemia_death_event_count.jpg'
        get_descripcion_diabetes = "La diabetes puede aumentar el riesgo de enfermedades cardíacas, incluido el fallo cardiaco, debido al daño que causa a los vasos sanguíneos y los nervios. Para mejorar la salud del corazón en personas con diabetes, es crucial controlar los niveles de azúcar en la sangre, la presión arterial y el colesterol, adoptar un estilo de vida saludable y seguir el plan de tratamiento recomendado."
        
        return {"graficas":get_graficas_anaemia,"descripciones":get_descripcion_diabetes}
    
    def get_grafica_y_descripcion_high_blood_pressure(self):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        
        # Generar la gráfica con Plotly Express
        fig = px.pie(df, values='high_blood_pressure',names='DEATH_EVENT', title='High Blood Pressure Death Event Ratio')
        fig.update_traces(textposition='inside', textinfo='percent+label') 
        fig.update_layout(
            title_text="Recuento de eventos de muerte por presión arterial alta"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/high_blood_pressure_death_event_count.jpg')
        get_graficas_high_blood_pressure = '/app/app/images/high_blood_pressure_death_event_count.jpg'
        get_descripcion_hight_blood_pressure = "La presión arterial alta sobrecarga el corazón y aumenta el riesgo de fallo cardiaco. Para mejorar, se pueden hacer cambios en el estilo de vida, como seguir una dieta baja en sodio, hacer ejercicio regularmente y reducir el estrés. Además, es importante seguir el plan de tratamiento médico según lo recetado."
        
        return {"graficas":get_graficas_high_blood_pressure,"descripciones":get_descripcion_hight_blood_pressure}
            
    