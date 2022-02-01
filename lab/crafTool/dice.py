import random

num_sixes = 0
num_sevens = 0
num_roles = int(input('Enter number or rolls:\n'))

if num_roles >= 1:
    for i in range(num_roles):
        die_one = random.randint(1, 6)
        die_two = random.randint(1, 6)
        roll_total = die_one + die_two

        # This is where the number is 6's are counted
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll {} is {} ({} + {})'.format(i, roll_total, die_one, die_two))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid entery for rolls. Please try again.')