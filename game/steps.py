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
          "They can walk the path with many      |\n"
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
          'but if they see you it\'s already to late.              |\n'
          '<-----------------------------------------------> ')
    print(Style.RESET_ALL)




# ------------ Pick your character
def get_char(hear):
    global choice
    choice = format(Fore.LIGHTMAGENTA_EX + choice + Style.RESET_ALL)
    print('Hello {}, pick your class'.format(choice))
    nomad()
    alchemist()
    berserker()

    list = {'A', 'N', 'B'}
    hear = "n".upper()  # input().upper

    if hear == 'A':
        print(choice, Fore.BLUE+ 'The Alchemist.' +Style.RESET_ALL)
    elif hear == 'N':
        print(choice,Fore.GREEN+ 'The Nomad' +Style.RESET_ALL)
    elif hear == 'B':
        print(choice, Fore.RED + 'The Berserker'+ Style.RESET_ALL)
    elif hear not in list:
        print('input worng')

    f = input('what now')


main_menu()
choice = "MidNightCookies"  # input()

# This can be done better with location


get_char(choice)
