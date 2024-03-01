from app.SparkServices.SparkServices import SparkServices

def test_run_analysis():
    spark_services = SparkServices()
    spark_services.get_grafica_age()
    spark_services.get_grafica_creatinine_phosphokinase()
    spark_services.get_grafica_ejection_fraction()
    spark_services.get_grafica_platelets()
    spark_services.get_grafica_serum_sodium()

test_run_analysis()
