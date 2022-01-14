import math
real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximately correct pi to within 2 decimal places

print('pi is {pi}'.format(pi=real_pi))
print('22/7 is {pi}'.format(pi=approximate_pi))
print('22/7 looks better like {pi:.2f}'.format(pi=approximate_pi))