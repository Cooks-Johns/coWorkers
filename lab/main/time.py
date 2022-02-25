class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


my_time = Time()
my_time.hours = 24
my_time.minutes = 60

print('{} hours'.format(my_time.hours), end=' ')
print('and {} minutes'.format(my_time.minutes))