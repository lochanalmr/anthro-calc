class Metrics:
    def __init__(self):
        self.bmi = None

    def bmi_calc(self, weight, height):
        self.bmi = weight / (height * height)
        return self.bmi