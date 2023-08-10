class AverageCalculator:
    def __init__(self, data):
        self.data = data

    def call(self):
        sum = 0
        for element in self.data:
            sum += element['grade']
        average = sum / len(self.data)
        return average
    