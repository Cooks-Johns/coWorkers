
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


def exact_change(total_change):

    num_dollars = total_change // 100
    dollar_change = total_change % 100

    if num_dollars == 1:
        print(str(num_dollars) + ' Dollar')
        exact_change(total_change - 1 * 100)
    elif num_dollars > 1:
        print(str(num_dollars) + ' Dollars')
        exact_change(total_change - num_dollars * 100)
    elif dollar_change >= 25:
        num_quarters = dollar_change // 25
        quarter_change = dollar_change % 25
        if num_quarters == 1:
            print(str(num_quarters) + ' Quarter')
            exact_change(total_change - 1 * 25)
        elif num_quarters > 1:
            print(str(num_quarters) + ' Quarters')
            exact_change(total_change - num_quarters * 25)
    elif dollar_change >= 10:
        num_dimes = dollar_change // 10
        dime_change = dollar_change % 10
        if num_dimes == 1:
            print(str(num_dimes) + ' Dime')
            exact_change(total_change - 1 * 10)
        elif num_dimes > 1:
            print(str(num_dimes) + ' Dimes')
            exact_change(total_change - num_dimes * 10)
    elif dollar_change >= 5:
        num_nickels = dollar_change // 5
        nickel_change = dollar_change % 5
        if num_nickels == 1:
            print(str(num_nickels) + ' Nickel')
            exact_change(total_change - 1 * 5)
        elif num_nickels > 1:
            print(str(num_nickels) + ' Nickels')
            exact_change(total_change - num_nickels * 5)
    elif dollar_change >= 1:
            num_pennies = dollar_change // 1
            if num_pennies == 1:
                print(str(num_pennies) + ' Penny')
                exact_change(total_change - 1 * 1)
            else:
                print(str(num_pennies) + ' Pennies')
                exact_change(total_change - num_pennies * 1)



total_change = 1

if total_change == 0:
    print('No change')

exact_change(total_change)

# exact_change(300)
#
# exact_change(141)


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