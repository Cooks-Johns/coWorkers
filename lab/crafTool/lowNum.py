num1 = 3
num2 = 3
num3 = 3

num_list = (num1, num2, num3)

# low_num = num1 if( (num1 < num2) and (num2 < num3) ) else num3
#
# print(low_num)

if num1 < num2 and num1 < num3:
    low = num1
elif num2 < num1 and num2 < num3:
    low = num2
elif num3 < num2 and num3 < num1:
    low = num3
else:
    low = num1

print(low)
