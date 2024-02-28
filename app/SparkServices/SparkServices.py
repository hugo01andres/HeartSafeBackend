from pyspark.sql import SparkSession
from matplotlib import pyplot as plt
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

    def get_prediction(self, age=None, anaemia=None, creatine_phosphokinase=None, diabetes=None, ejection_fraction=None, high_blood_pressure=None, platelets=None, serum_creatinine=None, serum=None):
        print("prediccion: ")
        print("get_prediction called")

    def get_graficas(self):
        try:
            df = self.spark.read.csv('file:////home/data/heart_failure_clinical_records_dataset.csv', header=True, inferSchema=True)
        except Exception as e:   
            print(f"file not found: {str(e)}")
            return 'File not found!', 404
        pandas_df = df.select('age').toPandas()
        
        # Crear la gráfica (ejemplo: histograma de la edad de los pacientes)
        plt.figure(figsize=(10, 6))
        plt.hist(pandas_df['age'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Distribution of Age in Heart Failure Patients')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        
        # Guardar la gráfica en un archivo PNG
        plt.savefig('/home/data/age_distribution_histogram.png')


        
        return "Grafica 1", "Grafica 2"
