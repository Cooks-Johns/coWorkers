# def steps_to_feet(num_steps):
# 	feet_per_step = 3
# 	feet = num_steps * feet_per_step
# 	return feet
#
#
# def steps_2_calories(num_steps):
# 	steps_per_minute = 70.0
# 	calories_per_minute_walking = 3.5
#
# 	minutes = num_steps / steps_per_minute
# 	calories = minutes * calories_per_minute_walking
# 	return calories
#
# steps = 1000 # This would be a int(input("How many steps did you walk"))
#
# feet = steps_to_feet(steps)
# print('feet:', feet)
#
# calories = steps_2_calories(steps)
# print('Calories:', calories)

# _-------------------
from colorama import Fore, Back, Style

# -----
def main_menu():
    print('              <--------------------------> ')
    print('             | Enter your Name, and press |')
    print('             | return to start your quest |')
    print('              <--------------------------> \n')





# -------------- Toons
def nomad():
    print(Fore.GREEN)
    print("'n'--> for Nomad __________________________________\n"
          "They have walked the path alone so    |\n"
          "make sure thier on your team          |\n"
          "<---------------------------------------->")
    print(Style.RESET_ALL)


def alchemist():
    print(Fore.BLUE)
    print('\'a\' for Alchemist______________________________\n'
          'The elixer is the the real gold,    |\n'
          'but gold is gold.                   |\n'
          '<-----------------------------------------------> ')
    print(Style.RESET_ALL)

def berserker():
    print(Fore.RED)
    print('\'b\' for Berserker______________________________________\n'
          'So this might be a good time to run....     |\n'
          'but if I it\'s already to late.              |\n'
          '<-----------------------------------------------> ')
    print(Style.RESET_ALL)




# ------------ Pick your character
def get_char(hear):

    print('Hello {}, who would you like to be'.format(choice))
    nomad()
    alchemist()
    berserker()

    list = {'a', 'n', 'c'}
    hear = "h"  # input().upper

    if hear == 'A':
        print('You are a Alchemist {}'.format(choice))
    if hear == 'N':
        print('Your are a Nomad {}'.format(choice))
    elif hear not in list:
        print('input worn')

choice = "MidNightCookies"  # input()

while choice != 'N':
    main_menu()
    # This can be done better with location
    choice = format(Fore.LIGHTMAGENTA_EX + choice + Style.RESET_ALL)
    get_char(choice)

    choice = 'Y'
print("later bro")