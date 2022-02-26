class TimeSetter():
    def __init__(self):
        self.min = 0
        self.hours = 0


time1 = TimeSetter()  # Create an instance of the Time class called time1

def min_hour():
    # Fixme make a conversion
    mins = 
    pass

def hour_min():
    pass

time1.hours = time1.min / 60
time1.min = 60

time2 = TimeSetter()  # Create a second instance called time2
time2.hours = 12
time2.min = 45

print('{} hours and {} minutes'.format(time1.hours, time1.min))
print('{} hours and {} minutes'.format(time2.hours, time2.min))