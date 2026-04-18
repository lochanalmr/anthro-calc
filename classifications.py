class Classifications:
    def __init__(self):
        self.bmi_class = None
        self.bai_class = None
        self.whr_class = None

    def bmi_classification(self, region, bmi):
        if region == 'O':
            if bmi <= 18.5:
                self.bmi_class = "Underweight"
            elif bmi < 25:
                self.bmi_class = "Normal"
            elif bmi < 30:
                self.bmi_class = "Overweight"
            else:
                self.bmi_class = "Obese"
        else:
            if bmi <= 18.5:
                self.bmi_class = "Underweight"
            elif bmi < 23:
                self.bmi_class = "Normal"
            elif bmi < 27:
                self.bmi_class = "Overweight"
            else:
                self.bmi_class = "Obese"
        return self.bmi_class

    def bai_classification(self, bai, gender, age):
        if gender == 'M':
            if age < 20:
                self.bai_class = "Unable to classify for people below 20 years old"
            elif age < 40:
                if bai < 8:
                    self.bai_class = "Underweight"
                elif bai < 21:
                    self.bai_class = "Normal"
                elif bai < 26:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            elif age < 60:
                if bai < 11:
                    self.bai_class = "Underweight"
                elif bai < 23:
                    self.bai_class = "Normal"
                elif bai < 29:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            elif age < 80:
                if bai < 13:
                    self.bai_class = "Underweight"
                elif bai < 25:
                    self.bai_class = "Normal"
                elif bai < 31:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            else:
                self.bai_class = "Unable to classify for people above 80 years old"

        elif gender == 'F':
            if age < 20:
                self.bai_class = "Unable to classify for people below 20 years old"
            elif age < 40:
                if bai < 21:
                    self.bai_class = "Underweight"
                elif bai < 33:
                    self.bai_class = "Normal"
                elif bai < 39:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            elif age < 60:
                if bai < 23:
                    self.bai_class = "Underweight"
                elif bai < 35:
                    self.bai_class = "Normal"
                elif bai < 41:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            elif age < 80:
                if bai < 25:
                    self.bai_class = "Underweight"
                elif bai < 38:
                    self.bai_class = "Normal"
                elif bai < 43:
                    self.bai_class = "Overweight"
                else:
                    self.bai_class = "Obese"
            else:
                self.bai_class = "Unable to classify for people above 80 years old"

        else:
            self.bai_class = "Classification error due to invalid input"
        return self.bai_class

    def whr_classification(self, whr, gender):
        if gender == 'M':
            if whr <= 0.95:
                self.whr_class = "Low Health Risk"
            elif whr <= 1:
                self.whr_class = "Moderate Health Risk"
            else:
                self.whr_class = "High Health Risk"

        elif gender == 'F':
            if whr <= 0.8:
                self.whr_class = "Low Health Risk"
            elif whr <= 0.85:
                self.whr_class = "Moderate Health Risk"
            else:
                self.whr_class = "High Health Risk"
        else:
            self.whr_class = "Classification error due to invalid input"
        return self.whr_class
