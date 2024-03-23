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
            title_text="Gender wise Age Spread - Male = 1 Female =0"
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
            title_text="Smoking Death Event Count"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/smoking_death_event_count.jpg')
        get_graficas_diabetes = '/app/app/images/diabetes_death_event_count.jpg'
        get_descripcion_diabetes = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        
        return {"graficas":get_graficas_diabetes,"descripciones":get_descripcion_diabetes}
    

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
            title_text="Anaemia Death Event Count"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/anaemia_death_event_count.jpg')
        get_graficas_anaemia = '/app/app/images/anaemia_death_event_count.jpg'
        get_descripcion_anaemia = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        
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
            title_text="Diabetes Death Event Count"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/diabetes_death_event_count.jpg')
        get_graficas_anaemia = '/app/app/images/anaemia_death_event_count.jpg'
        get_descripcion_anaemia = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        
        return {"graficas":get_graficas_anaemia,"descripciones":get_descripcion_anaemia}
    
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
            title_text="High Blood Pressure Death Event Count"
        ) 

        # Guardar la gráfica en un archivo JPEG
        pio.write_image(fig, '/app/app/images/high_blood_pressure_death_event_count.jpg')
        get_graficas_high_blood_pressure = '/app/app/images/high_blood_pressure_death_event_count.jpg'
        get_descripcion_hight_blood_pressure = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        
        return {"graficas":get_graficas_high_blood_pressure,"descripciones":get_descripcion_hight_blood_pressure}
            
    # def get_grafica_creatinine_phosphokinase(self):
    #     try:
    #         df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
    #     except Exception as e:   
    #         print(f"file not found: {str(e)}")
    #         return 'File not found!', 404
    #     pandas_df = df.select('creatinine_phosphokinase').toPandas()  
    #     # Crear la gráfica (ejemplo: histograma de la edad de los pacientes)
    #     plt.figure(figsize=(10, 6))
    #     plt.hist(pandas_df['creatinine_phosphokinase'], bins=20, color='skyblue', edgecolor='black')
    #     plt.title('Distribution of creatinine_phosphokinase in Heart Failure Patients')
    #     plt.xlabel('creatinine_phosphokinase')
    #     plt.ylabel('Frequency')
    #     plt.grid(axis='y', alpha=0.75)
    #     # Guardar la gráfica en un archivo PNG
    #     plt.savefig('/app/app/images/creatinine_phosphokinase_distribution_histogram.png')
    #     return "Grafica 1", "Grafica 2"
    
    # def get_grafica_ejection_fraction(self):
    #     try:
    #         df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
    #     except Exception as e:   
    #         print(f"file not found: {str(e)}")
    #         return 'File not found!', 404
    #     pandas_df = df.select('ejection_fraction').toPandas()        
    #     # Crear la gráfica (ejemplo: histograma de la edad de los pacientes)

    #     plt.figure(figsize=(10, 6))
    #     plt.hist(pandas_df['ejection_fraction'], bins=20, color='skyblue', edgecolor='black')
    #     plt.title('Distribution of ejection_fraction in Heart Failure Patients')
    #     plt.xlabel('ejection_fraction')
    #     plt.ylabel('Frequency')
    #     plt.grid(axis='y', alpha=0.75)

        
    #     plt.savefig('/app/app/images/ejection_fraction_distribution_histogram.png')
    #     return "Grafica 1", "Grafica 2"

    # def get_grafica_platelets(self):
    #     try:
    #         df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
    #     except Exception as e:   
    #         print(f"file not found: {str(e)}")
    #         return 'File not found!', 404
    #     pandas_df = df.select('platelets').toPandas()        
    #     # Crear la gráfica (ejemplo: histograma de la edad de los pacientes)

    #     plt.figure(figsize=(10, 6))
    #     plt.hist(pandas_df['platelets'], bins=20, color='skyblue', edgecolor='black')
    #     plt.title('Distribution of platelets in Heart Failure Patients')
    #     plt.xlabel('platelets')
    #     plt.ylabel('Frequency')
    #     plt.grid(axis='y', alpha=0.75)

        
    #     plt.savefig('/app/app/images/platelets_distribution_histogram.png')
    #     return "Grafica 1", "Grafica 2"
    
    # def get_grafica_serum_sodium(self):
    #     try:
    #         df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
    #     except Exception as e:   
    #         print(f"file not found: {str(e)}")
    #         return 'File not found!', 404
    #     pandas_df = df.select('serum_sodium').toPandas()        
    #     # Crear la gráfica (ejemplo: histograma de la edad de los pacientes)

    #     plt.figure(figsize=(10, 6))
    #     plt.hist(pandas_df['serum_sodium'], bins=20, color='skyblue', edgecolor='black')
    #     plt.title('Distribution of serum_sodium in Heart Failure Patients')
    #     plt.xlabel('serum_sodium')
    #     plt.ylabel('Frequency')
    #     plt.grid(axis='y', alpha=0.75)

        
    #     plt.savefig('/app/app/images/serum_sodium_distribution_histogram.png')
    #     return "Grafica 1", "Grafica 2"