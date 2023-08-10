class BestStudent:
    def __init__(self, data):
        self.data = data

    def call(self):
        max = 0
        for element in self.data:
            if element['grade'] > max:
                max = element['grade']
                name = element['name']
        return name