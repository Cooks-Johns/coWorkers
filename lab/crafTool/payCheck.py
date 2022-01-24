# FIXME make this into a loop
while True:
    #Problem:
    #   calculate the weekly paycheck for an
    #   employee based on how many hours they worked

    # TOdo in the future make it so that the user can just imput this
    base_wage = 20       # Employee pay before working week_hours
    week_hours = 40      # Hours needed to get overtime_wage
    overtime_wage = 30   # Pay for exceeding week_hours

    # Step 1: Prompt user - allow user to input
                # float so that if they worked not a full hour
                # FIXME check user input for valid input
    hours_worked = float(input("How many hours did you work this week?: "))


    # Step 2: calculate hours worked
    # Normal pay
    if hours_worked <= week_hours:
        payCheck = hours_worked * base_wage

    # Overtime pay
    elif hours_worked >= week_hours:
        base_pay = (week_hours * base_wage)
        pay_overtime = ((hours_worked - week_hours) * overtime_wage)
        payCheck = base_pay + pay_overtime


    # TOdo Make sure that when user inputs isn't correct
    #  the applications starts back at the prompt to enter input
    else:
        print("Invalaid entery, please try again. ")

    # Step 3: Return the users
    print("You have earned ${} this week".format(payCheck))
    print()
