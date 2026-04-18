from collector_functions import *
from calculations import *
from classifications import *

def bmi_module():
    print("\nBMI Calculation and Classification Module")

    user_data = BasicData()
    basic_data_dict = user_data.basic_data_col()
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

def bai_module():
    print("\nBAI Calculation and Classification Module")

    user_data = BasicData()
    basic_data_dict = user_data.basic_data_col()
    age = basic_data_dict["age"]
    gender = basic_data_dict["gender"]
    unit = basic_data_dict["unit"]

    print("\nMeasurement Data Collection for BAI")
    measurement_data = MeasurementData()
    height = measurement_data.height_col(unit)
    hipc = measurement_data.hipc_col(unit)

    metrics = Metrics()
    bai = metrics.bai_calc(height, hipc)
    print(f"\nBAI Value: {metrics.bai:.2f}")

    classifications = Classifications()
    classifications.bai_classification(bai, gender, age)
    print(f"BAI Classification: {classifications.bai_class}")