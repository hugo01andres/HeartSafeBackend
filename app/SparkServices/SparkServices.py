from pyspark.sql import SparkSession
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
class SparkServices:
    def __init__(self):
        print("SparkServices initialized")
        self.spark = SparkSession.builder.appName("Flask and Spark: ").master('spark://spark-master:7077').getOrCreate()

    def get_spark_session(self):
        print("get_spark_session called")

    
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





    def get_grafica_age(self):
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
        
        return "Grafica 1", "Grafica 2"
    
    def get_grafica_smooking(self):
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
        
        return "Grafica 1", "Grafica 2"

            
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