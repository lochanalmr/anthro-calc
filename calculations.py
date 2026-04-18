class Metrics:
    def __init__(self):
        self.bmi = None
        self.bai = None

    def bmi_calc(self, weight, height):
        self.bmi = weight / (height * height)
        return self.bmi

    def bai_calc(self, height, hipc):
        self.bai = hipc * 100 / (height ** 1.5) - 18
        return self.bai