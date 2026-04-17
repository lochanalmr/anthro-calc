from collector_functions import *
from calculations import *
from classifications import *

def bmi_module():
    print("\nBMI Calculation and Classification Module")

    user_data = BasicData()
    basic_data_dict = user_data.basic_data_col()
    age = basic_data_dict["age"]
    gender = basic_data_dict["gender"]
    region = basic_data_dict["region"]
    unit = basic_data_dict["unit"]

    print("\nMeasurement Data Collection for BMI")
    measurement_data = MeasurementData()
    height = measurement_data.height_col(unit)
    weight = measurement_data.weight_col(unit)

    metrics = Metrics()
    bmi = metrics.bmi_calc(weight, height)
    print(f"\nBMI Value: {metrics.bmi:.2f}")

    classifications = Classifications()
    classifications.bmi_classification(region, metrics.bmi)
    print(f"BMI Classification: {classifications.bmi_class}")