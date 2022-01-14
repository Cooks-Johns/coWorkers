# SAMPLE INPUTS

color = "yellow"
obj = "Daisy"
num = "6"


# Todo (1) ask user for two words and store as vars
#     output on a line
#     EX: You entered: yellow Daisy" 6
# color = input("Give me a color please:")
# obj = input("Give me a object please :")
# num = int(input("Give me a number: "))


# Todo (2) output two pass combos
#         EX: "First password:" yellow_Daisy
#             "Second password:" 6yellow6

print("You entered:", color, obj, num)
print('')
print("First password: {}_{}".format(color, obj))
print("Second password: {}{}{}".format(num, color, num))



# Todo (3) output the length of each
#         EX: "Number of characters in " yellow_Daisy: 12
#             "Number of characters in " 6yellow6: 8
outPut1 = int(len(color) + len(obj) + 1)
outPut2 = int(len(num) + len(color) + len(num))

print("-"*24)
print("You entered: {} {} {}".format(color, obj, num))
print('')
print("First password: {}_{}".format(color, obj), outPut1)
print("Second password: {}{}{}".format(num, color, num), outPut2)