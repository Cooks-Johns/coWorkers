# color = input()
# obj = input()
# num = input()
#
color = "yellow"
obj = "Daisy"
num = "6"

print("You entered: ", color, obj, num)
print("")
print("First password: ", color + "_" + obj)
print("Second password: ", num + color + num)
print("")

outPut1 = int(len(color) + len(obj) + 1)
outPut2 = int(len(num) + len(color) + len(num))

print("You entered: {} {} {}".format(color, obj, num))

print("")
print("First password:", color + "_" + obj)
print("Second password:", num + color + num)
print("")


print("Number of characters in {}_{}".format(color, obj) + ":", outPut1)
print("Number of characters in {}:".format(num + color + num), outPut2)
