# year = 2001
#
#
#
# =====================
# if year > 2101:
#     print("Distant future")
# elif year > 2001:
#     print("21st century")
# elif year >= 1901:
#     print("20th century")
# else:
#     print("Long ago")


# =====================
# special_list = [-99, 0, 44]
# special_num = int(input())
#
# if special_num in special_list:
#     print('Special number')
# else:
#     print('Not special number')


# =====================
# for temps
# temperatures = {
#     'Seattle': 56.5,
#     'New York': float(input()),
#     'Kansas City': 81.9,
#     'Los Angeles': 76.5
# }
#
# if "New York" in temperatures:
#     if temperatures["New York"] > 90:
#         print("The city is melting!")
#     else:
#         print("The temperature in New York is", temperatures["New York"])
# else:
#     print("The temperature in New York is unknown.")


# =====================
# Negative
# user_val = int(input()) # -9 0 3735
#
# cond_str = "negative" if(user_val <= -9) else "non-negative"
#
# print(user_val, 'is', cond_str)


#
#
# num_users = 8
# update_direction = 3
#
# num_users = (num_users + 1) if (update_direction == 3) else (num_users - 1)
#
# print('New value is:', num_users)



num1 = 29
num2 = 6
num3 = 17


#    7      15
if num1 <= num2:
    lownum = num1 #

#     15     3
elif num2 <= num3:
    print(num2)
else:
    print(num3)

low_num = num1 if( (num1 < num2) and (num2 < num3) ) else num3

if low_num:
    print(low_num)


print(low_num)