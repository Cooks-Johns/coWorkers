class PatientData:
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0
        self.age = 0


patient = PatientData()
print('Patient data (before):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs,', end=' ')
print(patient.age, 'age')


# TODo make a menu to convert this information
patient.height_inches = int(input('Enter height in inches: '))
patient.weight_pounds = int(input('Enter weight in pounds'))
patient.age = int(input('Enter your age in months'))

print('Patient data (after):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')