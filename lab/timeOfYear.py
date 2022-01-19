from time import strptime

# user_month = (input("Enter number for month: ")
# use_date = int(input("Enter number for date: "))
month_input = input("Enter a month: ")
user_date = int(input("Enter your date: "))
# month_num = strptime(month_input, "%b").tm_mon
#
# date = month_num, user_date
# print(date)
print(month_input)

if month_input == ("March" or "April" or "May" or "June"):
    print("Spring")
elif month_input == ("June", "July", "August", "September"):
    print("Summer")
elif month_input == ("September", "October", "November", "December"):
    print("Autumn")
elif month_input == ("December", "January", "Febuary", "March") and user_date < (19):
    print("Winter")
else:
    print("Invalid ")

