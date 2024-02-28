from app.SparkServices.SparkServices import SparkServices

def test_run_analysis():
    spark_services = SparkServices()
    spark_services.graficar_columnas()
    spark_services.guardar_graficos_en_carpeta()
    #spark_services.get_prediction(20, True, 100, True, 20, True, 200, 1, 1)

test_run_analysis()
