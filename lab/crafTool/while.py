# while loops

# curr_pow = 3
# user_ans = "y"
#
# while user_ans == "y":
#     print(curr_pow)
#     curr_pow = curr_pow * 2
#     user_ans = input()
#
# print("done")

# =================================
### Face
# nose = "0" # This will be a lil nose
# user_face = "-"
#
# while user_face != "q":
#     print(" {} {} ".format(user_face, user_face)) # This will print eyes
#     print("  {}  ".format(nose)) # This is for ths nose
#     print(user_face*5) # This is for the mouth
#     print("\n")
#
#     # Here is the part to get new characters for eyes and mouth
#     user_input = input("Enter a character ('q' for quit): \n")
#     user_face = user_input[0]
# print("See you later Big Dog!")

# =================================
# num = int(input())
# while num > 0:
#     print(num % 10)
#     num = num // 10
#     num = int(input())
# print("later bro!")

# =================================
### Find your ancestors

def numOfAncestors():
    year_considered = 2020 # Year being considered
    num_ancestors = 2 # Guess of ancestors in considered year
    year_per_generation = 20 # Approx. years per generation

    user_year = int(input("Enter a past year (neg. for B.C.): "))
    print()

    while year_considered >= user_year:
        print("Ancestors in {}: {}".format(year_considered, num_ancestors))

        num_ancestors = num_ancestors * 2
        year_considered = year_considered - year_per_generation

# =================================================================

# x = 0
# while x > 0:
#     print(x, end=' ')
#     x = x - 1
# print('Bye')
# ===========
#
# x = 5
# y = 18
# while y >= x:
#     print(y, end=' ')
#     y = y - x
# ===========
# x = 10
# while x != 3:
#     print(x, end=' ')
#     x = x / 2
# ===========
# x = 1
# y = 3
# z = 5
# while not (y < x < z):
#     print(x, end=' ')
#     x = x + 1
# ===========
# g = 2
#
# while g <= 5:
#     print(g, end=' ')
#     g += 1
# =================================================================
# this will contine until the var user_num is false
#  Keep in mind --> by putting a input in this it will stop it from
#       printing until the users next input
#
# user_num = 20
# while user_num >= 1:
#     user_num = user_num / 2
#     print(user_num)

# =================================================================
## Euclid's algorithm ----- Computes the greatest common divisor (GCD)

# num_a = int(input("Enter first positive integer: "))
# print()
#
# num_b = int(input("Enter second positive integer: "))
# print()
#
# while num_a != num_b:
#     if num_a > num_b:
#         num_a = num_a - num_b
#     else:
#         num_b = num_b - num_a
#
# print("GCD is {}".format(num_a))


# =================================================================
'''
# Chat
This program has a convo with the user
with the elif branch it uses a random number to
mix up the program's responses.
'''
# import random  # This is a library to generate random numbers
#
# print("Tell me something about yourself.")
# print("You can type \'Goodbye\' at anytime to quit.\n")
#
# user_text = input()
#
# while user_text != "Goodbye":
#     random_num = random.randint(0, 2) # Generate random int between 0/2
#     if random_num == 0:
#         print("\nPlease explain further.\n")
#     elif random_num == 1:
#         print("\nWhy do you say: '{}'?\n".format(user_text))
#     elif random_num == 2:
#         print('\nWhat else can you share?\n')
#     else:
#         print('\nUh-oh, something went wrong. Try again.\n')
#
#     user_text = input()
#
# print('It was nice talking with you. Goodbye.\n')

# =================================================================
''' Average of List with Sentinel
Output average of list of positive int
List ends with 0 ( sentinel )
Ex: 
    10
    1
    6
    3
    0
    
yields (10 + 1 + 6 + 3) / 4, or 5
Average: 5
'''
#
# values_sum = 0
# num_values = 0
#
# curr_val = int(input())
#
# while curr_val > 0:  # Get the values until 0 or <
#     values_sum += curr_val
#     num_values += 1
#     curr_val = int(input())
#
# print("Average: {:.0f}\n".format(values_sum / num_values))

# =================================================================
#### Bid bot random
# import random
# random.seed(5)
#
# keep_going = '-'
# next_bid = 0
#
# while keep_going == "-" or keep_going == "y":
#    next_bid = next_bid + random.randint(1, 10) # this makes the bid random but if can be made to to let user input bid
#    print('I\'ll bid ${}!'.format(next_bid))
#    print('Continue bidding?', end=' ')
#    keep_going = input()

#-------------
# FIXME
#
# num_insects = 8 # Must be >= 1
# print()
# bugs = 100
# while num_insects <= bugs:
#     print(num_insects * bugs)
#
#

#---



# I = 20
# N = 100
#
# while I > 0:
#     print(I)
#





# =================================================================
# Counting with a while
# Iterating N times using a loop variable
# i = 1
# while i <= N:
#     i = i + 1
#-----
# Savings Interest
# initial_savings = float(input("How much did you save? :"))
# interest_rate = float(input("How much is your interest rate? :"))
#
# initial_savings = 5000
# interest_rate = 0.03
#
# print("Initial savings of ${}".format(initial_savings))
# print("at {:.0f}% yearly interest.\n".format(interest_rate*100))
#
# years = int(input("Enter years: "))
# print()
#
# savings = initial_savings
# i = 1   # This will loop through the condition
# while i <= years:
#     print("Savings at beginning of year {}: ${:.2f}".format(i, savings))
#     savings = savings + (savings*interest_rate)
#     i = i + 1  # Variable that will increment loop
#
# print("\n")

# =========
### ---- Loop over presidential election years
# year = 1792
# current_year = 2021
#
# while year <= current_year:
#     print(year)
#     year = year + 4

# =================================================================
#--- Odds
# i = 1
# while i < 9:
#     i = i + 2
#     print(i)

#--- iTERATES OVER multiples
# i = 0
# while i <= 1000:
#     i = i + 5
#     print(i)
#--- Odds ints down form set int
# i = 211
# while i >= 31:
#     i = i - 2
#     print(i)

# outer_helper = 0
#
# while outer_helper < 3:
#     inner_helper = 0
#     while inner_helper < 3:
#         print("outer_helper is {} and inner_helper is {}".format(outer_helper, inner_helper))
#         inner_helper += 1
#     outer_helper += 1


# =================================================================
# #--- HangMan
# word = 'onomatopoeia'
# num_guesses = 10
#
# hidden_word = '-' * len(word)
#
# guess = 1
#
# while guess <= num_guesses and '-' in hidden_word:
#     print(hidden_word)
#     user_input = input('Enter a character (guess #{}): '.format(guess))
#
#     if len(user_input) == 1:
#         # Count the number of times the character occurs in the word
#         num_occurrences = word.count(user_input)
#
#         # Replace the appropriate position(s) in hidden_word with the actual character.
#         position = -1
#         for occurrence in range(num_occurrences):
#             position = word.find(user_input, position + 1)  # Find the position of the next occurrence
#             hidden_word = hidden_word[:position] + user_input + hidden_word[
#                                                                 position + 1:]  # Rebuild the hidden word string
#
#         guess += 1
#
# if not '-' in hidden_word:
#     print('Winner!', end=' ')
# else:
#     print('Loser!', end=' ')
#
# print('The word was {}.'.format(word))


# =================================================================
# #--- Passenger data
# Fixme use this for something else it just needs a lil rework

#
# menu_prompt = ('Available commands:\n'
#                '  (add) Add passenger\n'
#                '  (del) Delete passenger\n'
#                '  (print) Print passenger list\n'
#                '  (exit) Exit the program\n'
#                'Enter command:\n')
#
# destinations = ['PHX', 'AUS', 'LAS']
#
# destination_prompt = ('Available destinations:\n'
#                       '(PHX) Phoenix\n'
#                       '(AUS) Austin\n'
#                       '(LAS) Las Vegas\n'
#                       'Enter destination:\n')
#
# passengers = {}
#
# print('Welcome to Mohawk Airlines!\n')
# user_input = input(menu_prompt).strip().lower()
#
# while user_input != 'exit':
#     if user_input == 'add':
#         name = input('Enter passenger name: \n').strip().upper()
#         destination = input(destination_prompt).strip().upper()
#         if destination not in destinations:
#             print('Unknown destination. \n')
#         else:
#             passengers[name] = destination
# # Delete
#     elif user_input == 'del':
#         name = input('Enter passenger name: \n').strip().upper()
#         if name in passengers:
#             del passengers[name]
# # Print
#     elif user_input == 'print':
#         for passenger in passengers:
#             print('{} --> {}'.format(passenger.title(),passengers[passenger]))
#     else:
#         print('Unrecognized command, please try again.')
#
#     user_input = input('Enter command:\n').strip().lower()
