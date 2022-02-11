
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
riders_per_ride = 3

line = []
num_vips = 0

menu = ('(1) Reverse place in line.\n'
        '(2) Reverse place in VIP line.\n'
        '(3) Dispactch riders.\n'
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input =