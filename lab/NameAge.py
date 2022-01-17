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

while True:

# FIXME not sure how to make user input bold
    username = input("What is your name? ").capitalize()
    userAge = int(input("How old are you? "))
# Testing Todo when doing it like this doesn't work
    # not sure how to format user key input
#     testAge = color.BOLD + input("how old") + color.END
#     boldYear = str(calculateYear(testAge))

    boldYear = str(calculateYear(userAge))

    hi = "Hello " + username
    age = "You were born in " + boldYear + "."


    print(hi, "You were born in", age)
    print()

