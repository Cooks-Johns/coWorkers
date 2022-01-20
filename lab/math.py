import math



x = 2.3
ce = math.ceil(x)
print("ceil {}: round up value {}".format(x,ce))

floo = math.floor(x)
print("floor {}: round down value {}".format(x,floo))
print("-------------")
z = 4.5
powFloor = math.pow(math.floor(z), 2.0)
print("round down {}: then raised by the power of 2.0 returns {}".format(z,powFloor))

xzz = 15.75
xz = math.sqrt(math.ceil(xzz))
print("round up {}: then return {} as square root".format(xzz,xz))

fac = 4
facc = math.factorial(fac)
print("factorial (3! = 3 * 2 * 1) for input {} this returns {}".format(fac, facc))
