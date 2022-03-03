

'''

----% General Formula  %----
                        Yi + 1 = Yi + hf(Xi, Yi)
- where Yi + 1 is the next estiimated solution value
- Yi is the current value
- h is the interval between steps
- f(Xi, Yi) is the value of the derivative at the current (Xi, Yi) point

--- Functional value aat any point 'b', given by 'y(b)'
        n = (b-x0) / h
- Where
        n = number of steps
        h = interval width (size of each step)

    define f(x,y)
    input x0, y0
    input h, n
    for j from 0 to (n-1) do:
        Yj + 1 = Yj + hf(xj, yj)
        xj + 1 = xj + h
        print( xj + 1 and yj + 1 )


---> Links
https://ocw.mit.edu/courses/mathematics/18-03sc-differential-equations-fall-2011/unit-i-first-order-differential-equations/numerical-methods/eulers-method-1/
https://rsmith.math.ncsu.edu/MA573_F20/LECTURES/Lecture4.pdf
https://people.sc.fsu.edu/~jburkardt/py_src/euler/euler.py
https://people.sc.fsu.edu/~jburkardt/classes/math1902_2020/stiff/stiff.pdf

'''

# def Em(xi,yi,d,f):
#     x = xi
#     y = yi
#     n = round((f - xi) / d)
#
#     for j in range(n):
#         y = y + prime(f) * d
#         x = x + d
#         return y
#
# def prime(t):
#     return (9/2) * t + (3/2)
#
#
# print(Em(0, 2, 0.25, 4))

# -------------------------

def Em(xi,yi,d,f):
    x = xi
    y = yi

    n = round((f - xi) / d)
    d = (f - xi) / (n - 1)


    for i in range(n):
        y = prime(f) * (d + y)
        x += d
        return '{:.2f}'.format(y)

def prime(t):
    return (9/2) * t + (3/2)


print(Em(0, 2, 0.25, 4))




# ((d*y)