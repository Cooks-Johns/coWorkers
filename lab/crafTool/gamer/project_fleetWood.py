class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


time1 = Time()  # First instance of the Time class
time1.hours = 1
time1.minutes = 60

time2 = Time()  # Second instance
time2.hours = 48
time2.minutes = 180

print('1st: {} hours and {} minutes'.format(time1.hours, time1.minutes))
print('2nd: {} hours and {} minutes'.format(time2.hours, time2.minutes))