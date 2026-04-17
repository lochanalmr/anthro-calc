class Classifications:
    def __init__(self):
        self.bmi_class = None

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