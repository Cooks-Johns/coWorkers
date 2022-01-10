from datetime import date


while True:


    username = input("What is your name?")
    userAge = int(input("How old are you?"))

    class color:
        BOLD = '\033[1m'
        END = '\033[0m'

    def calculateYear(userAge):
        today = date.today()
        year = today.year - userAge
        return year


    boldYear = str(calculateYear(userAge))


    print("Hello", color.BOLD + username + color.END)
    print("You were born in",  color.BOLD + boldYear + color.END, ".")

# TODO In addition, submit a Microsoft Word document of 2 to 3 paragraphs explaining
# some of the features of PyCharm and why they can be useful.

# TODO
# TODO
# TODO