# ----- Acuction fees

'''
  Calculates fees charghed thru ebay.com given the selling price
  of fixed-price books, movies, music exct
  :param sell_price:
      feel is $.05 to list 13% of selling price
      up to $50.00
  :return:
      5% of amount from $50.01 to $1000
      2% of amount $1000.01 or more
  '''

# def cal_store_fee(sell_price):
#   p_under50 = .13             # for $50 and lower
#   p50_to_1000 = 0.05    # for $50.01 - $1000
#   p_under1000 = 0.02          # $1000.01 and higher
#   fee = 0.50          # fee to list item
#
#   if sell_price <= 50:
#       fee = fee + (sell_price * p_under50)
#   elif sell_price <= 1000:
#       fee = fee + (50 * p_under50) + \
#             ((1000 - 50) * p50_to_1000) + \
#             ((sell_price - 100) * p_under1000)
#       return fee
#
# selling_price = 100 # float(input('Enter item selling price (ex: 65.00): '))
# print('eBay fee: $ {}'.format(cal_store_fee(selling_price)))
#
# ----- Making User defined functions emprove readabality

# size = 5
#
# def get_nums(num):
#     numbers = []
#     usr_input = input('Enter {} integers:\n'.format(num))
#
#     i = 0
#     for token in usr_input.split():
#         number = int(token)     # Convert string input into int
#         numbers.append(number)  # Add to number list
#
#         print(i, number)
#         i += 1
#
#     return numbers
#
# def print_all_numbers(numbers):
#     # Print numbers
#     print('Numbers:')
#
# def print_odd_numbers(numbers):
#     # Print all odd numbers
#     print('Odd numbers:')
#
# def print_negative_numbers(numbers):
#     # Print all negative numbers
#     print('Negative numbers:')
#
# nums = get_nums(size)
# print_all_numbers(nums)
# print_odd_numbers(nums)
# print_negative_numbers(nums)


# ----- Popcorn
#
# def print_popcorn(bag_ounces):
#     m=6
#     if bag_ounces < 3:
#         bag = 'Too small'
#     elif bag_ounces >= 10:
#         bag = 'Too large'
#     else:
#         bag = '{} seconds'.format(bag_ounces * m)
#     print(bag)
#
# user_ounces = 7.42
# print_popcorn(user_ounces)

# ----- Shampoo

# def shampoo_instructions(num_cycles):
#     if num_cycles < 1:
#         num_cycles = 'Too few'
#         print(num_cycles)
#     elif num_cycles > 4:
#         num_cycles = 'Too many'
#         print(num_cycles)
#     else:
#         for x in range(1, num_cycles + 1):
#             print('{} : Lather and rinse.'.format(x))
#         print('Done.')
#
# user_cycles = 6
# shampoo_instructions(user_cycles)

# ----- --------- -- --- byte the code

# def add_up(x):
#     y = x + 1
#     return y
#
# print(add_up(4))

# # -----
# def human_head():
#     print('   ||||| ')
#     print('   o   o')
#     print('     >' )
#     print('   ooooo')
#     return
#
# def monkey_head():
#     print('   .-"-.')
#     print(' _/.-.-.\\_')
#     print('( ( o o ) )')
#     print(' |/  "  \\|')
#     print('  \\ .-. /')
#     print('  /`"""`\\')
#     return
#
# def print_figure(face):
#     face()  # Print the face
#     print('     |')
#     print('   --|--')
#     print('  /  |  \\')
#     print('@    |    @')
#     print('     |')
#     print('    /|\\')
#     print('   @   @')
#     return
#
# choice = int(input('Enter "1" to draw monkey, "2" for human: '))
#
# if choice == 1:
#     print_figure(monkey_head)
# elif choice == 2:
#     print_figure(human_head)
#
# ---

# def celsius_to_kelvin(value_celsius):
#     value_kelvin = 0.0
#
#     value_kelvin = value_celsius + 273.15
#     return value_kelvin
#
# def kelvin_to_celsius(value_kelvin):
#     value_celsius = 0.0
#
#     value_celsius = value_kelvin - 273.15
#     return value_celsius
#
# value_c = 10.0
# print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')
#
# value_k = 283.15
# print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')
#

# ## ------ We Going Global with these Variables

# emp_name = 'N/A'
#
# def get_nam():
#     # if this is not added the fuction with cast the origin value of emp_name
#     # --- Ex. Your name is: N/A
#     # global emp_name
#     name = input('whats your name homie\n')
#     emp_name = name
#
# get_nam()
# print('Your name is: {}'.format(emp_name))
#
#
''' 
Namespace = maps the visible names in a scope to object
scope = the area of code where a name is visible
locals() = Returns a dictionary of names found in local namespace
Scope resolution = The process of searching namespaces for a name

'''

###    -------                        game test
#

# from game.steps import *
#
# main_menu()
# choice = "MidNightCookies"  # input()
#
# # This can be done better with location
#
# get_char(choice)


###    -------

# import  random
#
# player_name = "Gandalfsta"
# player_type = 'Wizard'
#
# def roll(): # d20
#     number = random.randint(1,20)
#     return number
#
# print('A troll attacks')
# troll_roll = roll()
# player_roll = roll()
#
# print('Player: {} Troll: {}'.format(str(player_roll), str(troll_roll)))

###    -------

# def avg(a, b):
#     tmp = (a + b) / 2.0 # will create tmp in local namespace
#     return tmp

# def get_tmp():
#     a = 5
#     b = 10
#     tmp = a + b # This creates tmp in global namespace
#     # print('Avg: {:f}'.format(avg(a, b)))
#     print('Sum: {:f}'.format(tmp))
#
# get_tmp()
#
#

###    ------- arbitrary argument list

# def sandwich(bread, meat, *sauce):
#     print('{} on {}'.format(meat, bread), end=' ')
#     if len(sauce) > 0:
#         print('with', end=' ')
#     for extra in sauce:
#         print(extra, end=' ')
#     print("")
#
#
# sandwich('sourdough', 'turkey', 'mayo')
# sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')

###    -------
#
# def sandwich(bread, meat, **condiments):  ## **condiments can be any word
#     print('{} on {}'.format(bread, meat))
#     for category, extra in condiments.items():
#         print('   {}: {}'.format(category, extra))
#
# sandwich('sourdough', 'turkey', sauce='mayo')
# sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')
#
#



def nums(user_val1, user_val2):
    tem = user_val1
    user_val1 = user_val2
    user_val2 = tem
    # lis = '{} {}'.format(user_val2, user_val1)
    print(user_val1, user_val2)

x, y = 2, 4


nums(x, y)
nums(-1, 10)
nums(9, 0)
nums(11, 11)
