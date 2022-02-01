# =================================================================

# ------ Normal for loop

def revenueDaWeek():
    daily_revenues = [
        2356.23,  # Monday
        1800.12,  # Tuesday
        1792.50,  # Wednesday
        2058.10,  # Thursday
        1988.00,  # Friday
        2002.99,  # Saturday
        1890.75   # Sunday
    ]

    total = 0
    for day in daily_revenues:
        total += day

    average = total / len(daily_revenues)

    print('Weekly revenue: ${:.2f}'.format(total))
    print('Daily average revenue: ${:.2f}'.format(average))

# =================================================================
# Reversed Loops
def reversedLoop():
    names = [
        'Biffle',
        'Bowyer',
        'Busch',
        'Gordon',
        'Patrick'
    ]
    for name in names:
        print(name, '|', end=' ')
    print('\nPrinting in reverse:')
    #---
    for name in reversed(names):
        print(name, '|', end=' ')


    temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
    num_neg = 0
    for temp in temperatures:
        if temp < 0:
            num_neg += 1
    print(num_neg)

# =================================================================
#Fixme
#\
def contactsEmail():
    contact_emails = {
        'Sue Reyn' : 's.reyn@email.com',
        'Mike Filt': 'mike.filt@bmail.com',
        'Nate Arty': 'narty042@nmail.com'
    }

    new_contact = "Mark"
    new_email = "email"
    contact_emails[new_contact] = new_email

    for contact_emails in reversed(contact_emails):
        print(new_email, 'is', new_contact)


# =================================================================
### NESTED LOOPS
"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
# print('Two-letter domain names:')
#
# letter1 = 'a'
# letter2 = '?'
# while letter1 <= 'z':  # Outer loop
#     letter2 = 'a'
#     while letter2 <= 'z':  # Inner loop
#         print('{}{}.com'.format(letter1, letter2))
#         letter2 = chr(ord(letter2) + 1)
#     letter1 = chr(ord(letter1) + 1)
# =========
# Histogram
# num = 0
# while num >= 0:
#     num = int(input('Enter an integer (negative to quit) :\n'))
#
#     if num >= 0:
#         print('Depicted graphically:')
#         for i in range(num):
#             print('*', end='')
#         print('\n')
#
# print('Goodbye.')
#
# =========

# c1 = 'a'
# while c1 < 'b':
#     c2 = 'a'
#     while c2 <= 'c':
#         print('{}{}'.format(c1, c2), end=' ')
#         c2 = chr(ord(c2) + 1)
#     c1 = chr(ord(c1) + 1)

# =========
#
# i1 = 1
# while i1 < 19:
#     i2 = 3
#     while i2 <= 9:
#         print('{}{}'.format(i1,i2), end=' ')
#         i2 = i2 + 3
#     i1 = i1 + 10
## ======
# num_rows = 33
# num_cols = 21
#
# for i in range(num_rows):
#     print('*', end=' ')
#     for j in range(num_cols-1):
#         i*=j
#
#         print('*', end=' ')
#     print()

# =================================================================
### Taco break
#
# empanada_cost = 3
# taco_cost = 4
#
# user_money = int(input('Enter money for meal: '))
#
# max_empanadas = user_money // empanada_cost
# max_tacos = user_money // taco_cost
#
# meal_cost = 0
# for num_tacos in range(max_tacos + 1):
#     for num_empanadas in range(max_empanadas + 1):
#         meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)
#
#         # Find first meal option that exactly matches user money
#         if meal_cost == user_money:
#             break
#
#     # Find first meal option that exactly matches user money
#     if meal_cost == user_money:
#         break
#
# if meal_cost == user_money:
#     print('${} buys {} empanadas and {} tacos without change.'
#         .format(meal_cost, num_empanadas, num_tacos))
# else:
#     print('You cannot buy a meal without having change left over.')

# # =======
### Taco continue

def empanadaTaco():
    empanada_cost = 3
    taco_cost = 4

    user_money = int(input('Enter money for meal: '))

    num_diners = int(input('How many people are eating: '))

    max_empanadas = user_money // empanada_cost
    max_tacos = user_money // taco_cost

    meal_cost = 0
    num_options = 0
    for num_tacos in range(max_tacos + 1):
        for num_empanadas in range(max_empanadas + 1):

            # Total items purchased must be equally divisible by number of diners
            if (num_tacos + num_empanadas) % num_diners != 0:
                continue

            meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

            if meal_cost == user_money:
                print('${} buys {} empanadas and {} tacos without change.'
                      .format(meal_cost, num_empanadas, num_tacos))
                num_options += 1

    if num_options == 0:
        print('You cannot buy a meal without having change left over.')


# ===============================================
# Simon Says

# user_score = 0
# simon_pattern = input()
# user_pattern  = input()
#
# simon = ('R','G','B','Y')
#
#
#
# print('User score:', user_score)


# ===============================================

def test():
    choice = ''

    while choice != "quit":
        while True:
            print("1. Fun story")

            choice2 = int(input("Which template of madlib would you like to play (Enter the number of your choice) "))
            break  # This break will take you out of this while loop to reach if/else

        if choice2 == 1:
           noun1 = input("Enter a noun: ")
           plural_noun = input("Enter a plural noun: ")
           noun2 = input("Enter another noun: ")
           print("Be kind to your {}-footed {} a day keep the doctor away.".format(noun1, plural_noun, noun2))

        else:
            choice = "quit"


# ===============================================