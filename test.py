from app.SparkServices.SparkServices import SparkServices
from app.IAServices.IAServices import IAServices

def test_run_analysis():
    spark_services = SparkServices()
    spark_services.get_graficas()
    # spark_services.probar_test()
    ia_services = IAServices()
    ia_services.make_pdf(1, 2, 3)
    pass
    #spark_services.get_prediction(20, True, 100, True, 20, True, 200, 1, 1)

test_run_analysis()
