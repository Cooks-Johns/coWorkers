# Todo

# testing
# 49
# 155
# 148
# 60
# outPut-> Calories: 736.21 calories

# todo old
# age = int(input())
# weight = float(input())
# heartRate = float(input())
# time = float(input())
#
# women_calories_str = ((age * 0.074) - (weight * 0.05741) + (heartRate * 0.4472) - 20.4022) * time / 4.184
# men_calories_str = ((age * 0.2017) + (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * time / 4.184
#
# women_calories = "{:.2f}".format(women_calories_str)
# men_calories = "{:.2f}".format(men_calories_str)
#
#
# print('Women:', str(women_calories), 'calories')
# print('Men:', str(men_calories), 'calories')


# -- TODO NEW --

''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 '''


''' Type your code here. '''

age = int(input("How old are you? :"))
weight = float(input("What is your weight? :"))
heartRate = float(input("What is your heart rate? :"))
time = float(input("How many mins did you workout? :"))

calories = ((age * 0.2757)
            + (weight * 0.03295)
            + (heartRate * 1.0781) - 75.4991) * time / 8.368

print('Calories: {:.2f} calories'.format(calories))