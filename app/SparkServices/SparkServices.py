from pyspark.sql import SparkSession
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
        print("Grafica 1")
        print("Grafica 2")
        print("get_graficas called")
        return "Grafica 1", "Grafica 2"
