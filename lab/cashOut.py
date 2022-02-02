
# Dollars, Quarters, Dimes, Nickels, and Pennies

dollar = 1.
quarter = .25
dime = .10
nickel = .05
pennie = .01

# change = float(input("How much is your change? :"))

#

money = 389
bag = {}


# if money <= 0:
#     print("no charge")
#     exit(0)
#
# if money >= 100:
#     # money = money - money[0:1]
#     bag.append("{} dollars".format(money[0]))
#
# print(bag)


def printCurrency(total_change):
    dollar = total_change // 100
    dollar_change = total_change % 100

    if dollar == 1:
        print(str(dollar) + 'Dollar')
        printCurrency(total_change - 1 * 100)
    elif dollar > 1:
        print(str(dollar) + ' Dollars')
        printCurrency(total_change - dollar * 100)
    elif dollar_change >= 25:
        quarter = dollar_change // 25
        quarter_change = dollar_change % 25
        if quarter == 1:
            print(str(quarter) + ' Quarter')
            printCurrency(total_change - 1 * 25)
        elif quarter > 1:
            print(str(quarter) + ' Quarters')
            printCurrency(total_change - quarter * 25)
    elif dollar_change >= 10:
        dime = dollar_change // 10
        dime_change = dollar_change % 10
        if dime == 1:
            print(str(dime) + ' Dime')
            printCurrency(total_change - 1 * 10)
        elif dime > 1:
            print(str(dime) + ' Dimes')
            printCurrency(total_change - dime * 10)
    elif dollar_change >= 5:
        nickel = dollar_change // 5
        nickel_change = dollar_change % 5
        if nickel == 1:
            print(str(nickel) + ' Nickel')
            printCurrency(total_change - 1 * 5)
        elif nickel > 1:
            print(str(nickel) + ' Nickels')
            printCurrency(total_change-nickel * 5)
    elif dollar_change >= 1:
            penny = dollar_change // 1
            if penny == 1:
                print(str(penny) + ' Penny')
                printCurrency(total_change - 1 * 1)
            else:
                print(str(penny) + ' Pennies')
                printCurrency(total_change - penny * 1)



total_change = 0
if total_change == 0:
    print('No change')
printCurrency(total_change)


#
# dollar = total_change // 100
# dollar_change = total_change % 100
#
# bag = 0
# if total_change <= 0:
#     print('No change')
#
#
# if dollar == 1:
#     print(str(dollar) + ' Dollar')
#     bag = total_change - 1 * 100
# elif dollar > 1:
#     print(str(dollar) + ' Dollars')
#     total_change = total_change - dollar * 100
#
#
# elif dollar_change >= 25:
#     quarter = dollar_change // 25
#     quarter_change = dollar_change % 25
# if quarter == 1:
#     print(str(quarter) + ' Quarter')
#     total_change = total_change - 1 * 25
# elif quarter > 1:
#     print(str(quarter) + ' Quarters')
#     total_change = total_change - quarter * 25
# elif dollar_change >= 10:
#     dime = dollar_change // 10
#     dime_change = dollar_change % 10
#
# #
# #
# # if dime == 1:
# #     print(str(dime) + ' Dime')
# #     printCurrency(total_change - 1 * 10)
# # elif dime > 1:
# #     print(str(dime) + ' Dimes')
# #     printCurrency(total_change - dime * 10)
# # elif dollar_change >= 5:
# #     nickel = dollar_change // 5
# #     nickel_change = dollar_change % 5
# #
# #
# #
# # if nickel == 1:
# #     print(str(nickel) + ' Nickel')
# #     printCurrency(total_change - 1 * 5)
# # elif nickel > 1:
# #     print(str(nickel) + ' Nickels')
# #     printCurrency(total_change - nickel * 5)
# # elif dollar_change >= 1:
# #     penny = dollar_change // 1
# #     if penny == 1:
# #         print(str(penny) + ' Penny')
# #         printCurrency(total_change - 1 * 1)
# #     else:
# #         print(str(penny) + ' Pennies')
# #         printCurrency(total_change - penny * 1)
#
# print(total_change)
# print(dollar_change)