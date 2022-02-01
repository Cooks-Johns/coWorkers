

# earth_g = 9.81  # m/s^2
# mars_g = 3.71
#
# if __name__ == '__main__':
#     print('Earth constant:', earth_g)
#     print('Mars constant:', mars_g)

#====================================================
import math

# x = 2.3
# 3
# z = math.ceil(x)

# z = math.floor(x) # 2

# math.floor(z) returns 4. Then, math.pow(4,2.0) returns
# z = 4.5
# z = math.pow(math.floor(z), 2.0) # 16.0

# z = 15.75
# z = math.sqrt(math.ceil(z)) # 4.0

# z = 4
# z = math.factorial(z) # 24
#
# print(z)

import math

point_dist = 0.0


x1 = 1.0
y1 = 2.0
x2 = 1.0
y2 = 5.0

point_dist = math.pow((x2 - x1) + (y2 -y1))

print('Points distance:', point_dist)