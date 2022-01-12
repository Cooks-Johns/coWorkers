from datetime import date



   # username = input("What is your name?")

class color:
    BOLD = '\033[1m'
    END = '\033[0m'

def calculateYear(userAge):
    if userAge <= 0:
        return userAge
    today = date.today()
    year = today.year - userAge
    return year

#TODo how to check

def checker(x):

    if username is None or len(username) and userAge <= 0:
        return username




## END
while True:


    username = input("What is your name? ").capitalize()
    checker()
    userAge = int(input("How old are you? "))
    calculateYear()
    boldYear = str(calculateYear(userAge))

    hi = "Hello {}!"
    age = "You were born in {}."

    print(hi.format(color.BOLD + username + color.END),
          "You were born in", age.format(color.BOLD + boldYear + color.END))
    print()


# TODO
# TODO
# TODO  firstUpper = username.capitalize()
#  --
