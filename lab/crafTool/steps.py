
def steps_to_feet(num_steps):
	feet_per_step = 3
	feet = num_steps * feet_per_step
	return feet


def steps_2_calories(num_steps):
	steps_per_minute = 70.0
	calories_per_minute_walking = 3.5

	minutes = num_steps / steps_per_minute
	calories = minutes * calories_per_minute_walking
	return calories

steps = 1000 # This would be a int(input("How many steps did you walk"))

feet = steps_to_feet(steps)
print('feet:', feet)

calories = steps_2_calories(steps)
print('Calories:', calories)