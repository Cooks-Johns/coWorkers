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

# ----- 