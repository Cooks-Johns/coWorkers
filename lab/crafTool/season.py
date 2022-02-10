

seasons = [
    "January", "Febuary", "March",
    "April", "May", "June",
    "July", "August", "September", "October",
    "November", "December"
]

spring = ["March", "April", "May", "June"]
# if march is > 20 and June is < 20

summer = ["June", "July", "August", "September"]
# if June is > 21 and September is < 21

autumn = ["September", "October", "November", "December"]
# if September is > 22 and December is < 20

winter = ["December", "January", "Febuary", "March"]
# if December is > 21 and March is < 19

day = [*range(1,31)]



# Take 3
month_input = 'August'  #input()
day_input = 11  # int(input())

    #

while month_input in seasons:
    print(month_input)
    if month_input == "March" and day_input > 20:

    month_input = input()
print("Error")



    #
    # if day_input not in day:
    #     seasons = "wrong day"
    #
    #
    # if month_input == "April" or "May":
    #     seasons = "Spring"
    #
    # elif month_input == "July" or "August":
    #     seasons = "Summer"
    #
    # elif month_input == "October" or "November":
    #     seasons = "Autumn"
    #
    # elif month_input == "January" or "Febuary":
    #     seasons = "Winter"
    #
    #
    #
    # if month_input == "March":
    #     if day_input >= 20:
    #         seasons = "Spring"
    #     elif month_input == "March":
    #             if day_input <= 19:
    #                 seasons = "Winter"
    #
    #
    #
    # if month_input == "June":
    #     if day_input >= 21:
    #         seasons = "Summer"
    #     elif month_input == "June":
    #         if day_input <= 20:
    #             seasons = "Spring"
    #
    #         if month_input == "September":
    #             if day_input <= 21:
    #                 seasons = "summer"
    #
    # if month_input == "September":
    #     if day_input >= 22:
    #         if month_input == "December":
    #             if day_input <= 20:
    #                 seasons = "Autumn"
    #
    # if month_input == "December":
    #     if day_input >= 21:
    #         if
    #
    # print(seasons)