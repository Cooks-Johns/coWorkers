
# FIXME these guys need a lil rework so that you can use this in other locations

user_int = int(input("Enter integer (32 - 126):\n"))
user_float = float(input("Enter float:\n"))
user_char = input("Enter character:\n")
user_str = input("Enter string:\n")


# FIXME these guys need a lil rework
int_char = chr(user_int)


# reading other items into variables, then output the four values on a
print(user_int, user_float, user_char, user_str)

# Output the four values in reverse
print(user_str, user_char, user_float, user_int)

# Convert the integer to a characer, and output that character
print(user_int, 'converted to a character is', int_char)


# Testing
# 99
# 3.77
# z
# Howdy
