# from time import strptime
#
# # user_month = (input("Enter number for month: ")
# # use_date = int(input("Enter number for date: "))
# month_input = input("Enter a month: ")
# user_date = int(input("Enter your date: "))
# # month_num = strptime(month_input, "%b").tm_mon
# #
# # date = month_input, user_date
# # # print(date)
# # print(month_input)
# #
# if month_input == ("March" or "April" or "May" or "June"):
#     if user_date <= 20:
#         print("Spring")
# elif month_input == ("June", "July", "August", "September"):
#     if user_date <= 21:
#         print("Summer")
# elif month_input == ("September","October", "November", "December"):
#     if user_date <= 22:
#         print("Autumn")
# elif month_input == ("December", "January", "Febuary", "March") and user_date < (19):
#     if user_date <= 21:
#        print("Winter")
# else:
#     print("Invalid ")
#
# Take 2
from datetime import datetime
#
# month_input = 'September'  #input()
# day_input = -1  # int(input())
#
# if month_input in ('January', 'February', 'March'):
#     season = 'Winter'
# elif month_input in ('April', 'May', 'June'):
#     season = 'Spring'
# elif month_input in ('July', 'August', 'September'):
#     season = 'Summer'
# elif month_input in ('September', 'October', 'November', 'December'):
#     season = 'Autumn'
#     if (month_input == 'March') and (day_input > 19 and day_input < 30):
#         season = 'Spring'
#     elif (month_input == 'June') and (day_input > 20 and day_input < 30):
#         season = 'Summer'
#     elif (month_input == 'September') and (day_input > 21 and day_input < 31):
#         season = 'Autumn'
#     elif (month_input == 'December') and (day_input > 1 and day_input < 30):
#         season = 'Winter'
#     else:
#          season = "Invalid"
#
# print(season)
#


# Take 3
month_input = 'June'  #input()
day_input = 21  # int(input())

days = int(day_input)
# if month_input == ('January', 'February', 'March') and (day_input > 19 and day_input < 30):


seasons = [
    "January", "Febuary", "March",
    "April", "May", "June",
    "July", "August", "September", "October",
    "November", "December"
]
day = [*range(1,31)]


spring = "March", "April", "May", "June"
# if march is > 20 and June is < 20

summer = "June", "July", "August", "September"
# if June is > 21 and September is < 21

autumn = "September", "October", "November", "December"
# if September is > 22 and December is < 20

winter = "December", "January", "Febuary", "March"
# if December is > 21 and March is < 19

# Check user input
if day_input in day and month_input in seasons:
    month_input = month_input
    day_input = day_input
else:
    print("error")

# Check user season
# Spring
# if month_input in spring and month_input == "April" or "May":
#     print("Spring")
# elif month_input == "March" and day_input > 20:
#     print("Spring")
# elif month_input == "June" and day_input <= 20:
#     print("Spring")
# # Summer
# if month_input in summer and month_input == "July" or "August":
#     print("Summer")
# if month_input == "June" and day_input > 21:
#     print("Summer")
# elif month_input == "September" and day_input < 21:
#     print("Summer")

# print user season

if month_input in spring:
    seasons = "Spring"
elif month_input in summer:
    seasons = "Summer"
elif month_input in autumn:
    seasons = "Autumn"
else:
    seasons = "Winter"

#Spring
if seasons == "April" or "May":
    seasons = "Spring"
    if seasons == "March" and day_input > 20 or seasons == "June" and day_input < 20:
        seasons = "Spring"

#Summer
if seasons == "July" or "August":
    seasons = "Summer"
    if seasons == "June" and day_input > 21 or seasons == "September" and day_input < 21:
        seasons = "Summer"


#Autumn
if seasons == "October" or "November":
    seasons = "Autumn"
    if seasons == "September" and day_input > 22 or seasons == "December" and day_input < 20:
        seasons = "Autumn"


# Winter
if seasons == "January" or "Febuary":
    seasons = "Winter"
    if seasons == "December" and day_input > 21 or seasons == "March" and day_input < 19:
        seasons = "Winter"

print(seasons)