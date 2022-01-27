# year = 2001
#
#
#
# =====================
# if year > 2101:
#     print("Distant future")
# elif year > 2001:
#     print("21st century")
# elif year >= 1901:
#     print("20th century")
# else:
#     print("Long ago")



# =====================
# Welcome to the Python 500 race! Click the run button to begin.

# Configurable values.
# Try changing car speeds, accelerations, and the simulation speed.
# car1_top_speed = 60
# car2_top_speed = 50
#
# car1_acceleration = 11
# car2_acceleration = 10
#
# car1 = ['  ______\n',
#         ' |__1_|_\\\n',
#         '  O----O\n']
#
# car2 = ['    ___\n',
#         '   /__2_\\__\n',
#         '    O----O\n']
#
# # Begin program below.
#
# # Track the location and speed of each car
# car1_location = 0
# car2_location = 0
# car1_speed = 0
# car2_speed = 0
#
# track_length = 1000  # Length of the race
# cols = 60  # Width of the output window
#
#
# def print_car(car, distance):
#     """Print a car at a scaled distance from the left side of the screen"""
#     scale = float(distance) / float(track_length) * cols
#     for line in car:
#         print(' ' * int(scale), line, end=' ')
#
#
# def print_cars():
#     """Print each of the racing cars"""
#     print_car(car1, car1_location)
#     print_car(car2, car2_location)
#
#
# def max_car_len():
#     return max(max([len(i) for i in car1], [len(i) for i in car2]))
#
#
# def print_finish():
#     """Print the finish line"""
#     ln = "||--FINISH LINE--||"
#     print(' ' * (cols + max_car_len() - len(ln)), end=' ')
#     print(ln)
#
#
# def advance_cars():
#     """Calculate new positions of the cars"""
#     global car1_speed, car1_location
#     global car2_speed, car2_location
#     car1_speed += car1_acceleration
#     car1_speed = car1_top_speed if car1_speed > car1_top_speed else car1_speed
#     car1_location += car1_speed
#
#     car2_speed += car2_acceleration
#     car2_speed = car2_top_speed if car2_speed > car2_top_speed else car2_speed
#     car2_location += car2_speed
#
#
# def finished():
#     """Check for a winner"""
#     if car1_location > track_length or car2_location > track_length:
#         if car1_location > car2_location:
#             win_distance = car1_location - car2_location
#             print('Car 1 wins by', win_distance, 'meters!')
#         else:
#             win_distance = car2_location - car1_location
#             print('Car 2 wins by', win_distance, 'meters!')
#         return True
#     return False
#
#
# while not finished():
#     """Main loop"""
#     advance_cars()
#
# print_cars()
# print_finish()
#


# =====================
# special_list = [-99, 0, 44]
# special_num = int(input())
#
# if special_num in special_list:
#     print('Special number')
# else:
#     print('Not special number')


# =====================
# for temps
# temperatures = {
#     'Seattle': 56.5,
#     'New York': float(input()),
#     'Kansas City': 81.9,
#     'Los Angeles': 76.5
# }
#
# if "New York" in temperatures:
#     if temperatures["New York"] > 90:
#         print("The city is melting!")
#     else:
#         print("The temperature in New York is", temperatures["New York"])
# else:
#     print("The temperature in New York is unknown.")


# =====================
# Negative
# user_val = int(input()) # -9 0 3735
#
# cond_str = "negative" if(user_val <= -9) else "non-negative"
#
# print(user_val, 'is', cond_str)


#
#
# num_users = 8
# update_direction = 3
#
# num_users = (num_users + 1) if (update_direction == 3) else (num_users - 1)
#
# print('New value is:', num_users)


#
# num1 = 29
# num2 = 6
# num3 = 17
#
#
# #    7      15
# if num1 <= num2:
#     lownum = num1 #
#
# #     15     3
# elif num2 <= num3:
#     print(num2)
# else:
#     print(num3)
#
# low_num = num1 if( (num1 < num2) and (num2 < num3) ) else num3
#
# if low_num:
#     print(low_num)
#
#
# print(low_num)

# =====================

## Calculate how long it takes to get somewhere

# miles = float(input('Enter a distance in miles: '))
# hours_to_fly = miles / 500.0 # this is the speed of the plain
# hours_to_drive = miles / 60.0 # this is the speed of the car
#
# print(miles, 'miles would take:')
# print(hours_to_fly, 'hours to fly')
# print(hours_to_drive, 'hours to drive')

# playing with floating-paoint literal and scientific notation

# ma = float(1.0e-4) # 0.0001
# print(ma)

# ka = float(7.2e-4) # 0.00072
# print(ka)

# pa = float(6.02e23) # 6.02e+23
# print(pa)

# ag = float(6.23596e2) # 623.596

# print(ag)



# =====================
# ++  Energy to mass conversion ++

# c_meters_per_sec = 299792458  # Speed of light (m/s)
# joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
# joules_per_TNT_ton = 4.184e9
#
# #Read in a floating-point number from the user
# mass_kg = float(input("Lets use a float to check your energy: "))
#
# #Compute E = mc^2.
# energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
# print('Total energy released:', energy_joules, 'Joules')
#
# #Calculate equivalent number of AA and tons of TNT.
# num_AA_batteries = energy_joules / joules_per_AA_battery
# num_TNT_tons = energy_joules / joules_per_TNT_ton
#
# print('Which is as much energy as:')
# print('  ', num_AA_batteries, 'AA batteries')
# print('  ', num_TNT_tons, 'tons of TNT')

# # ===================== Sphere volume
# # sphere = (4.0 / 3.0)πr3
# area = float(input())
# gallons_paint = area/350
#
# pi = 3.14159
# sphere_volume = 0.0
#
# sphere_radius = float(input())
# sphere_volume = 4.0/3.0*pi*sphere_radius**3
# print('Sphere volume: {:.2f}'.format(sphere_volume))



# # ===================== Acceleration of gravity
# G = 6.673e-11
# M = 5.98e24
# accel_gravity = 0.0
#
# dist_center = 6.3782e6 #float(input())
#
# accel_gravity = (G*M)/(dist_center**2)
#
# print('Acceleration of gravity: {:.2f}


#----------------------------------------- Getting digits
# p = 100 % (1 // 2)
# print(p)


# x = 2
# y = 2 * (x + 8)
#
# print(x, y)

#
# x = 1
# y = (3 * (x + 1)) + 5
#
# print(x, y)

# x = 6
# y = x / 2
#
# print(x, y)

# x = 19
# y = x % 3
#
# print(x, y)

# a = 3
# x = 4
# y = a * x
# y = y + 6
#
# print(x, y)
#====================================================
# user_val = float(input())
# #
# ones_digit = user_val % 10    # Ex: 927 % 10 is 7.
# tmp_val = user_val // 10
#
# tens_digit = tmp_val % 10     # Ex: tmp_val = 927 // 10 is 92. Then 92 % 10 is 2.
# tmp_val = tmp_val // 10
#
# hundreds_digit = tmp_val % 10     # Ex: tmp_val = 92 // 10 = 9. Then 9 % 10 is 9
#
# # tmp_val =      phone_num // 10000  # // 10000 shifts right by 4, so 936555.
# # prefix_num =   tmp_val % 1000 # % 1000 gets the right 3 digits, so 555.
#
# print(ones_digit)


#====================================================
# Minutes to hours/minutes
# minutes = int(input("Enter minutes: \n"))
# hours = minutes // 60
# minutes_remaining = minutes % 60
#
# print(minutes, 'minutes is ', end='')
# print(hours, 'hours and ', end='')
# print(minutes_remaining, 'minutes.\n', end='')


#====================================================
# Minutes to hours/minutes


# dollar = float(input("Enter your bill"))
# penny = dollar // 1
# nickle = dollar // 5
# dime = dollar // 10
# quarter = dollar // 25
#
#
#

#====================================================
#
# amount_to_change = 9
#
# num_fives = amount_to_change // 5
#
# num_ones = amount_to_change % 5
# print('Change for $', amount_to_change)
# print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')

#====================================================
#



