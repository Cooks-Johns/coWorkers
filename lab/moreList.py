
# my_list = [1, 2, 3]
# del my_list[1]
# print(my_list)
#
#
# # Mod List
# user_input = 'Gertrude Sam Ann Joseph'
# short_names = user_input.split()
#
# del short_names[0]       # Delete item on list
# short_names[2] = 'Joe'      # Mod item on list
# print(short_names)


# here are some list methods

# --------       Adding Elements
# my_list = [5, 8]
#- Append
# my_list.append(16)

#- Extend
# my_list.extend([4, 12])

#- Insert
# my_list.insert(1, 1.7)

# ---           Removing Elements
# my_list = [5, 8, 14]
# #- Remove --> first item
# # my_list.remove(8)
#
# #- Pop --> last item
# # my_list.pop()
#
# #- pop(i) --> return item at position i
# val = my_list.pop(0)
# print(val)
# print(my_list)

# ---           Modifying Elements

# my_list = [14, 5, 8]

#- Sort itesm by value low to high NO String
# my_list.sort()

#- Reverse elements in place
# my_list.reverse()

#- list.index(x) -- Return idex for first item of list with value x
# print(my_list.index(14))

#- list.count(x) -- Count how many times x is in list
# print(my_list.count(5))
#
# print(my_list)

#----
# riders_per_ride = 3
#
# line = []
# num_vips = 0
#
# menu = ('(1) Reverse place in line.\n'
#         '(2) Reverse place in VIP line.\n'
#         '(3) Dispactch riders.\n'
#         '(4) Print riders.\n'
#         '(5) Exit.\n\n')
#
# user_input = input(menu).strip().lower()
#
# while user_input != '5':
#         if user_input == '1': #Add Rider
#                 name = input('Enter name:').strip().lower()
#                 print(name)
#                 line.append(name)
#
#         elif user_input == '2':
#                 print('Fixme ')
#                 print('FIXME: Add new VIP')
# # FIXME Add new rider behind last VIP in line
# #  Hint: Insert the VIP into the line at position num_vips.
# #       Don't forget to increment num_vips.
#
#         elif user_input == '3':  # Dispatch ride
#                 print('FIXME: Remove riders from the front of the line.')
# # FIXME Remove last riders_per_ride from front of line.
# #  Don't forget to decrease num_vips, if necessary.
#
#         elif user_input == '4':  # Print riders waiting in line
#                 print('{} person(s) waiting:'.format(len(line)), line)
#
#         else:
#                 print('Unknown menu option')
#
#         user_input = input('Enter command: ').strip().lower()
#         print(user_input)
#
# temps = [65, 67, 72, 75]
# temps.append(77)
# print(temps[-1])
#
# actors = ['Pitt', 'Damon']
# actors.insert(1, 'Affleck')
# print(actors[0], actors[1], actors[2])

#
# my_list.sort() # -- sort then
# my_list.pop() # --- remove the greates value




# ---- Iterating - Maximum even Num

# User inputs string w/ numbers: '203 12 5 800 -10'
# user_input = [23, 234, 687, 99, 3, 87,23, 67] # input('Enter numbers:')
#
# tokens = user_input#.split()  # Split into separate strings
#
#
# # ------ Convert strings to integers
# nums = []
# for token in tokens:
#     nums.append(int(token))
#
# print(tokens)

# ------ Print each position and number
# print()  # Print a single newline
# for index in range(len(nums)):
#     value = nums[index]
#     print('{}: {}'.format(index, value))


# ------ Determine maximum even number
# max_num = None
# for num in nums:
#     if (max_num == None) and (num % 2 == 0):
#         # First even number found
#         max_num = num
#     elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
#         # Larger even number found
#         max_num = num

# print('Max even #:', max_num)


# -- Count odd numbers
# nums = 23, 21, 92, 2, 91, -23
# cnt_odd_nums = 0
# for i in nums:
#         if i % 2 == 1:
#                 cnt_odd_nums += 1
#
# print(cnt_odd_nums)

#- Count Negitive numbers
# cnt_neg_nums = 0
# for i in nums:
#         if i < 0:
#                 cnt_neg_nums += 1
# print(cnt_neg_nums)

#- What can be be divided
# div_by = 10
# div_num = 0
# for i in nums:
#         if i % div_by == 0:
#                 div_num += 1
# print(div_num)


#---  finding the sum of a list elements

# User inputs string w/ numbers: '203 12 5 800 -10'
# user_input = input('Enter numbers: ')
#
# tokens = user_input.split()  # Split into separate strings
#
# # Convert strings to integers
# print()
# nums = []
# for pos, token in enumerate(tokens):
#     nums.append(int(token))
#     print('{}: {}'.format(pos, token))
#
# sum = 0
# for num in nums:
#     sum += num
#
# print('Sum:', sum)
#

# my_list = [0, 5, 10, 15]
# sums = any(my_list)
# print(sums)

# Max even
# def max_even():
#     nums = [1, 44, 15, 24]
#     max_even = None
#     for num in nums:
#         if num % 2 == 0:
#             if max_even == None or num > max_even:
#                 max_even = num
#                 print(max_even)
# max_even()
# num = [2, -43, 9, -2, -58]
# cnt_neg = 0
# for i in num:
#     if i < 0:
#         cnt_neg += 1
#     print(cnt_neg)



# ---- Grades
#
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
# menu_prompt = (" 1. Add/modify student grade \n"
#                 "2. Delete student grade \n"
#                 "3. Print student grades \n"
#                 "4. Quit\n")
#
# while True:  # Exit when user enters no input
#     command = input(menu_prompt).lower().strip()
#     if command == '1':
#         name, grade = input(grade_prompt).split()
#     # elif command == '2':
#     #     # ...
#     elif command == '3':
#         print(student_grades)
#     # elif command == '4':
#     #     break
#     else:
#         print('Unrecognized command.')
#

# my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
#
# # my_dict.update(dict(soda=1.49, burger=3.69))
# # burger_price = my_dict.get('burger', 0)
# # print(burger_price)
#
# my_dict['burger'] = my_dict['sandwich']
# val = my_dict.pop('sandwich')
# print(my_dict['burger'])


##-- List slicing
# nums = [1, 1, 2, 3, 5, 8, 13]
# # print(nums[1:5])
# #-  [1, 2, 3, 5]
# print(nums[5:10])
# # [8, 13]
# print(nums[3:-1])
# # [3, 5, 8]
###
# nums = [0, 25, 50, 75, 100]
# print(nums[0:5:2])
# # [0, 50, 100]
# print(nums[0:-1:3])
# [0, 75]

#--
# my_list = [5, 10, 20, 40, 80]
# # my_list[start:end]
# print('{}\n'.format(my_list))
# print('From start to end minus 1: {}'.format(my_list[0:2]))
#
# # my_list[start:end:stride]
# print('Every stride element from start to end minus1: {}'.format(my_list[0:5:3]))
#
# # my_list[start:]
# print('Start to end of list: {}'.format(my_list[0:5:3]))
# # my_list[:end]
# print('Form beginning of list to end with minus one: {}'.format(my_list[:4]))
# # my_list[:]
# print('beginning of list ends minus 1: {}'.format(my_list[:]))
#----

# nums = [10, 20, 30, 40, 50]
#
# for pos, value in enumerate(nums):
#     tmp = value / 2
#     if (tmp % 2) == 0:
#         nums[pos] = tmp
# print(nums[1])
#
# my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# print('1) ',my_list[:20])
# print('2) ',my_list[2:5])
# print('3) ',my_list[3:6])
# print('4) ',my_list[3:1])
# print('5) ',my_list[len(my_list)//2:(len(my_list)//2) + 1])
# print('6) ',my_list[4:])

# Adding to every element
# my_list = [-5, -4, -3]
# my_list = [(i+10) for i in my_list]
# print(my_list)

# Convert each num to a float
# my_list = [5, 20, 50]
# my_list = [float(i) for i in my_list]
# print(my_list)

# user input tnot a list of ints
# usr_input = input('Enter nums:')
# my_list = [int(i) for i in usr_input.split()]
# print(my_list)

#  Sum of rows in two-d list
# my_list = [[5, 10], [1]]
# sum_list = [sum(row) for row in my_list]
# print(sum_list)


# Sum of the row with the smallest sum in a two-D table
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = sum
# min_row = min([sum(row) for row in my_list])
print(sum_list)

# Twice the vallue
# [i*2 for i in x]

#Absolute
