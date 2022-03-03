

def EulerMod(x_init, y_init, delta, x_final):
    x = x_init
    y = y_init
    n = round((x_final - x_init) / delta)



    for j in range(n):
        y = y + primeq(x) * delta
        x = x + delta
        return y


def primeq(t):
    return (9/2) * t + (3/2)



print(EulerMod(0,2,0.25,4))

