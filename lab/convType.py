

# FIXME these guys need a lil rework so that you can use this in other locaaations
# def convType():
#     while True:
#         try:
#             user_int = int(input('Enter integer (32 - 126):\n'))
#             if user_int <= 32 or user_int >= 126:

# convType()
user_int = int()

user_float = float(input("Enter float:\n"))
user_char = input("Enter character:\n")
user_str = input("Enter string:\n")


# FIXME these guys need a lil rework
int_char = chr()
user_int = int()



# FIXME (1): Finish reading other items into variables, then output the four values on a
#  single line separated by a space
print(user_int, user_float, user_char, user_str)

# FIXME (2): Output the four values in reverse
print(user_str, user_char, user_float, user_int)

# FIXME (3): Convert the integer to a characer, and output that character
print(user_int, 'converted to a character is', int_char)


# Testing
# 99
# 3.77
# z
# Howdy


# TODO

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
