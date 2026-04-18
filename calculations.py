class Metrics:
    def __init__(self):
        self.bmi = None
        self.bai = None
        self.whr = None

    def bmi_calc(self, weight, height):
        self.bmi = weight / (height * height)
        return self.bmi

    def bai_calc(self, height, hipc):
        self.bai = hipc * 100 / (height ** 1.5) - 18
        return self.bai

    def whr_calc(self, waist, hipc):
        self.whr = waist / hipc
        return self.whr