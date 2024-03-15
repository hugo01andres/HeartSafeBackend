from app.SparkServices.SparkServices import SparkServices

def test_run_analysis():
    spark_services = SparkServices()
    spark_services.get_grafica_age()
    spark_services.get_grafica_smooking()
    spark_services.get_grafica_anaemia()
    spark_services.get_grafica__diabetes()
    spark_services.get_grafica_high_blood_pressure()

test_run_analysis()
