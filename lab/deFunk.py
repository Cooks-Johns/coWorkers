import math


# By passing pizza_diameter as a parameter you are able to call it as
# a argument that is provided to a function's parameter during a function  call
# def print_pizza_area(pizza_diameter):
#     pi_val = 3.14159265
#     # pizza_diameter = 12.0
#     pizza_radius = pizza_diameter / 2.0
#     pizza_area = pi_val * pizza_radius * pizza_radius
#     print('{:.1f} inch pizza is {:.3f} inches squared'
#           .format(pizza_diameter, pizza_area))

# print_pizza_area(12.0)
# print_pizza_area(16.0)
#---------------------------------------------
# functions with multiple parameters

# def print_pizza_volume(pizza_diameter, pizza_height):
#     pi_val = 3.14159265
#
#     pizza_radius = pizza_diameter / 2.0
#     pizza_area = pi_val * pizza_radius * pizza_radius
#     pizza_volume = pizza_area * pizza_height
#     print('{:.1f} x {:.1f} inch pizza is {:.3f} inches cubed.'
#           .format(pizza_diameter, pizza_height, pizza_volume))
#
# print_pizza_volume(12.0, 0.3)
# print_pizza_volume(12.0, 0.8)
# print_pizza_volume(16.0, 0.8)


# ---------------------------------------------
# def print_sum(num1, num2):
#     print(num1, '+', num2, 'is', (num1 + num2))
#
# print_sum(1, 2)
# ---------------------------------------------
#
# def print_age(user_age):
#     print('You are {}'.format(user_age))
#
# age_to_print = 24
# print_age(age_to_print)

# -------

# def print_price(price):
#     print('Price: ${}'.format(price))
#
# product_price = 16
# tax_amount = 2
# print_price(product_price + tax_amount)

# -------
# def print_operation(number1, number2):
#     print('{} - {} = {}'.format(number1, number2, number1 - number2))
#
# even_number = 2
# odd_number = 3
# print_operation(even_number, odd_number)
#
# -------
#
# def print_info(name, age):
#     print('{}, {}'.format(name, age))
#
#
# user_name1 = 'May'
# user_name2 = 'Max'
# user_age1 = 18
# user_age2 = 19
#
# print_info(user_name1, user_age1)
# print_info(user_name2, user_age2)

# -------

# def print_points(name, age, total_points):
#     print('{} is {}'.format(name, age))
#     print('{} made {} points'.format(name, total_points))
#
# user_name = 'May'
# user_age = 22
# regular_time_points = 22
# overtime_points = 4
#
# print_points(user_name, user_age, regular_time_points + overtime_points)

# ---------------------------------------------
#
# def output_minutes_as_hours(orig_minutes):
#     print(orig_minutes / 60)
#
# minutes = 210.0
# output_minutes_as_hours(minutes)
# ---------------------------------------------
#
# def print_total_inches(num_feet, num_inches):
#     print((num_feet * 12) + num_inches)
#
# feet = 5
# inches = 6
# print_total_inches(feet, inches)

# ---------------------------------------------
#
# def compute_square(num_to_square):
#     return num_to_square * num_to_square
#
#
# num_squared = compute_square(7)
#
# print

# ---------------------------------------------
# def square_root(x):
#     return math.sqrt(x)
#
# def print_val(x):
#     print(x)
#
# y = square_root(49.0)
#
# print(y)

# ---------------------------------------------
# # Celsius to Fahrenheit
# def c_to_f(c):
#     m = (9/5)
#     f = c * m + 32
#     return f
#
# temp_c = 32.3
# temp_f = None
#
# c_to_f(temp_c)
# print(temp_c)
# print('Fahrenheit:', temp_f)
#
# ---------------------------------------------

# def change_value(x):
#     return x + 3
#
# print(change_value(3))

# ------------

# def change_value(x):
#     return x + 4
#
# print(change_value(1))
#
#
# def change_values(x, y):
#     return x + y
#
# print(change_values(3, 4))

# def change_values(x, y):
#     newValue = x + y
#     return newValue
#
# print(change_values(4, 2))


# ---------------------------------------------


# def find_max(num_1, num_2):
#    max_val = 0.0
#
#    if (num_1 > num_2):  # if num1 is greater than num2,
#       max_val = num_1   # then num1 is the maxVal.
#    else:                # Otherwise,
#       max_val = num_2   # num2 is the maxVal
#    return max_val
#
# max_sum = 0.0
#
#
# num_a = 5.0
# num_b = 10.0
# num_y = 3.0
# num_z = 7.0
#
# max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)
# print('max_sum is:', max_sum)

# ---------------------------------------------
# Volume of a pyramid
#
# def pyramid_volume(base_length, base_width, pyramid_height):
#     m = 1/3
#     base_area = base_length * base_width * m
#     v = base_area * pyramid_height
#     return v
#
# length = 4.5
# width = 2.1
# height = 3.0
# print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))

# def add(x, y):
# 	return x + y
#
# def subtract(x, y):
# 	return x - y
#
# def mutiply(x, y):
# 	return x * y
#
#
# print('add(5, 7) is', add(5, 7))
# print("add('Tora', 'Bora') is", add('Tora', 'Bora'))
# print(add)
# ---------------------------------------------

#
# def mph_and_minutes_to_miles(hours_travled, miles_traveled):
#
#     hours_traveled = minutes_traveled / 60.0
#     miles_traveled = hours_traveled * miles_per_hour
#
#     return miles_traveled
#
#
# miles_per_hour = 70.0
# minutes_traveled = 100.0
#
# print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))

# ---------------------------------------------
# Incremental dev = writing a small amout of code then test, then a small amout more
#     #  and incremental amount is written and tested and so on
#
# def steps_to_feet(num_steps):
#     feet_per_step = 3
#     feet = num_steps * feet_per_step
#     return feet
#
# def step_to_cal(num_step):
#     pass
#
# def steps_to_calories(steps):
#     print('FIXME: finish steps_to_calories')
#     return steps - 1
#
# # T
# steps = 2344
#
# feet = steps_to_feet(steps)
# print('Feet:', feet)
#
# calories = step_to_cal(steps)
# print('Cal:', calories)
#
# step = steps_to_calories(steps)
# print('step', step)
# # ---------------------------------------------

# NotImplementedError - this is used to stop a program from running
# if a unfinished function is called this is used with the
#  'raise' this keyword

#
# def get_points(num_points):
#     """Get num_points from the user. Return a list of (x,y) tuples."""
#     raise NotImplementedError
#
#
# def side_length(p1, p2):
#     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
#
# def get_perimeter_length(points):
#     perimeter = side_length(points[0], points[1])
#     perimeter += side_length(points[0], points[2])
#     perimeter += side_length(points[1], points[2])
#     return perimeter
#
#
# coordinates = get_points(3)
# print('Perimeter of triangle:', get_perimeter_length(coordinates))
#
#



 # ---------------------------------------------
# def get_user_num():
#     print('FIXME: finish get_user_num()')
#     return - 1
#
# def compute_avg():
#     print('FIXME: compute_avg()')
#     return - 1
#
# user_num1 = 0
# user_num2 = 0
# avg_result = 0
#
# user_num1 = get_user_num()
# user_num2 = get_user_num()
# avg_result = compute_avg(user_num1, user_num2)
#
# print('Avg:', avg_result)

