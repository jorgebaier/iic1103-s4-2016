
def f(x):       # x es un parametro (que es una variable local)
    y = 10
    z = y
    zp = y
    return x*x + z

def esTrio(x,y,z):
    return x*x + y*y == z*z

print(f(1))
print(esTrio(3,4,5))

