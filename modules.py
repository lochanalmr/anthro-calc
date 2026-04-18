from collector_functions import *
from calculations import *
from classifications import *
from datetime import datetime
from anthrocalc import VERSION

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

def multimeasure_module():
    print("\nAnthroCalc MultiMeasure Module")

    user_data = BasicData()
    basic_data_dict = user_data.basic_data_col()
    age = basic_data_dict["age"]
    gender = basic_data_dict["gender"]
    region = basic_data_dict["region"]
    unit = basic_data_dict["unit"]

    print("\nMeasurement Data Collection for MultiMeasure")
    measurement_data = MeasurementData()
    height = measurement_data.height_col(unit)
    weight = measurement_data.weight_col(unit)
    waistc = measurement_data.waistc_col(unit)
    hipc = measurement_data.hipc_col(unit)

    metrics = Metrics()
    classes = Classifications()

    print(f"\nBMI Value: {metrics.bmi_calc(weight, height):.2f}")
    print(f"BMI Classification: {classes.bmi_classification(region, metrics.bmi)}")

    print(f"\nBAI Value: {metrics.bai_calc(height, hipc):.2f}")
    print(f"BAI Classification: {classes.bai_classification(metrics.bai, gender, age)}")

    print(f"\nWHR Value: {metrics.whr_calc(waistc, hipc):.2f}")
    print(f"WHR Classification: {classes.whr_classification(metrics.whr, gender)}")
    print()

    report_gen_choice = ""
    while report_gen_choice == "":
        report_gen_choice = input("Would you like to export this report as a text file (Y: Yes / N: No)?: ")
        if report_gen_choice != "" and report_gen_choice != None:
            report_gen_choice = report_gen_choice.upper()
            if report_gen_choice != "Y" and report_gen_choice != "N":
                report_gen_choice = ""
                continue

            if report_gen_choice == "Y":
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f'anthrocalc_mm_{timestamp}.txt'

                with open(filename, 'w') as file:
                    file.write(f"AnthroCalc v{VERSION} MultiMeasure Report")

                    file.write(f"\nBMI Value: {metrics.bmi}")
                    file.write(f"\nBMI Classification: {classes.bmi_class}")

                    file.write(f"\n\nBAI Value: {metrics.bai}")
                    file.write(f"\nBAI Classification: {classes.bai_class}")

                    file.write(f"\n\nWHR Value: {metrics.whr}")
                    file.write(f"\nWHR Classification: {classes.whr_class}")

                    file.write(f"\n\nReport generated at {timestamp}")
                    file.write(f"\nAnthroCalc v{VERSION}")
                
                print(f"{filename} was successfully exported to the same folder this program ran from")