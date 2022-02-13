
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

