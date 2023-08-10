from file_reader import FileReader
from average_calculator import AverageCalculator
from best_student import BestStudent


reader = FileReader('notas.csv')
data = reader.read_file()

average_calculator = AverageCalculator(data)
average = average_calculator.call()

best_student_calculator = BestStudent(data)
student = best_student_calculator.call()

print(average)
print(student)
