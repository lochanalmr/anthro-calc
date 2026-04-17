class BasicData:
    def __init__(self):
        self.age = None
        self.region = None
        self.gender = None
        self.unit = None
    
    def age_col(self):
        while True:
            try:
                self.age = int(input("Age: "))
                break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.age
    
    def region_col(self):
        while True:
            try:
                region = input("Region (A: Asia / O: Other): ")
                region = region.upper()
                if region == "A" or region == "O":
                    self.region = region
                    break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.region
    
    def gender_col(self):
        while True:
            try:
                gender = input("Gender (M: Male / F: Female): ")
                gender = gender.upper()
                if gender == "M" or gender == "F":
                    self.gender = gender
                    break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.gender

    def unitsys_col(self):
        while True:
            try:
                unit = input("Unit System (M: Metric / I: Imperial): ")
                self.unit = unit.upper()
                if self.unit == "M" or self.unit == "I":
                    break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.unit
    
    def basic_data_col(self):
        print("\nBasic Data Collection")
        self.age_col()
        self.region_col()
        self.gender_col()
        self.unitsys_col()
        return {
            "age": self.age,
            "region": self.region,
            "gender": self.gender,
            "unit": self.unit
        }


class MeasurementData:
    def __init__(self):
        self.height = None
        self.weight = None
        self.hipc = None
        self.waistc = None
    
    def height_col(self, unit):
        while True:
            try:
                height = float(input("Height: "))
                if unit == "I":
                    height = height / 39.37
                if unit == "M":
                    while True:
                        try:
                            cm_or_m_choice = input("[m] or [cm]: ")
                            if cm_or_m_choice == "cm" or cm_or_m_choice == "m":
                                break
                            else:
                                continue
                        except KeyboardInterrupt:
                            break
                    if cm_or_m_choice == "cm":
                        height = height / 100
                self.height = height
                break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.height
    
    def hipc_col(self, unit):
        while True:
            try:
                hipc = float(input("Hip Circumference: "))
                if unit == "I":
                    hipc = hipc / 39.37
                if unit == "M":
                    while True:
                        try:
                            cm_or_m_choice = input("[m] or [cm]: ")
                            if cm_or_m_choice == "cm" or cm_or_m_choice == "m":
                                break
                            else:
                                continue
                        except KeyboardInterrupt:
                            break
                    if cm_or_m_choice == "cm":
                        hipc = hipc / 100
                self.hipc = hipc
                break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.hipc
    
    def waistc_col(self, unit):
        while True:
            try:
                waistc = float(input("Waist Circumference: "))
                if unit == "I":
                    waistc = waistc / 39.37
                if unit == "M":
                    while True:
                        try:
                            cm_or_m_choice = input("[m] or [cm]: ")
                            if cm_or_m_choice == "cm" or cm_or_m_choice == "m":
                                break
                            else:
                                continue
                        except KeyboardInterrupt:
                            break
                    if cm_or_m_choice == "cm":
                        waistc = waistc / 100
                self.waistc = waistc
                break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.waistc
    
    def weight_col(self, unit):
        while True:
            try:
                weight = float(input("Weight: "))
                if unit == "I":
                    weight = weight / 2.205
                self.weight = weight
                break
            except KeyboardInterrupt:
                break
            except:
                continue
        return self.weight