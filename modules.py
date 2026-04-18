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
    metrics.bmi_calc(weight, height)
    print(f"\nBMI Value: {metrics.bmi:.2f}")

    classes = Classifications()
    classes.bmi_classification(region, metrics.bmi)
    print(f"BMI Classification: {classes.bmi_class}")

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
    metrics.bai_calc(height, hipc)
    print(f"\nBAI Value: {metrics.bai:.2f}")

    classes = Classifications()
    classes.bai_classification(metrics.bai, gender, age)
    print(f"BAI Classification: {classes.bai_class}")

def whr_module():
    print("\nWaist to Hip Ratio Calculation and Classification Module")

    user_data = BasicData()
    basic_data_dict = user_data.basic_data_col()
    age = basic_data_dict["age"]
    gender = basic_data_dict["gender"]
    unit = basic_data_dict["unit"]

    print("\nMeasurement Data Collection for BAI")
    measurement_data = MeasurementData()
    waist = measurement_data.waistc_col(unit)
    hipc = measurement_data.hipc_col(unit)

    metrics = Metrics()
    whr = metrics.whr_calc(waist, hipc)
    print(f"\nWaist to Hip Ratio Value: {metrics.whr:.2f}")

    classes = Classifications()
    classes.whr_classification(whr, gender)
    print(f"Waist to Hip Ratio Classification: {classes.whr_class}")