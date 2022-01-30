
# string = input("Please enter your own String : ")
# char = input("Please enter your own Character : ")

#
# # take input
# string = ("n It's a sunny day")
# #
# # # split list
# x = string.split()
# print(x)
# #
# # # remove frist item
# char = x[0]
# print(char)
#
#
#
# #
#
# cnt = count_Occurrence(char, string)
# print(cnt)
# # todo
# # ask user for character and phrase
# # take first letter of string and check it
# # todo

#
# string = input()

# split list
# x = string.split()
#
# # remove frist item
# char = x[0]
# count = string.count(x[0])
# print(str(count - 1 ))
# print(string)
#

#
#
#
# user_text = "Listen, Mr. Jones, calm down."
#
#
# # user_text = user_text.split(' ')
#
#
# user_text = user_text.split(',')
#
# print(user_text)
#
# # user_text = user_text.split('.')
# # print(user_text)
#


user_text = 'Listen, Mr. Jones, calm down.'
if "." in user_text:
    tokens = user_text.split('.')
    user_text = ''.join(tokens)
if "," in user_text:
    tokens = user_text.split(',')
    user_text = ''.join(tokens)
if " " in user_text:
    tokens = user_text.split(' ')
    user_text = ''.join(tokens)

how_long = len(user_text)

print(user_text, how_long)