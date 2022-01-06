#
#
# TODO
welcome = "Welcome homie "
age_input = "How old are you? :"
leave = "The kids table is over there lol"


# TODO
wat_name = "Hello there, so what is your name? :"
user_welcome = ""
wrong_str = "Please check string something doesn't look right"
wrong_str_len = "Please check the lenght of string"

# TODO
none_int = "Not a number please try again"
none_float = "Please enter a decimal"

# TODO

def yesNO(yn):
    if yn == 'yes' or 'y':
      return yn == True
    elif yn == 'no' or 'n':
       return yn == False
    return yesNO(yn)


while True:
    try:
        age = int(input(age_input))
        if age >= 18:
            print(welcome)
            # break;
        else:
            print(leave)
            continue
    except ValueError:
        print(none_int)
        continue

# TODO
    try:
        user_name = input(wat_name)
        if len(user_name) <= 12:
            print(welcome, )
            # break;
        else:
            print(wrong_str_len)
    except ValueError:
        print(wrong_str)





