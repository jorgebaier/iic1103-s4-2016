def suma(v1,v2):
    v = Vector(v1.x+v2.x, v1.y+v2.y)
    return v

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,v):
        return Vector(self.x+v.x, self.y+v.y)

    def __add__(self,v):
        return Vector(self.x+v.x, self.y+v.y)

    def __sub__(self,v):
        return Vector(self.x-v.x, self.y-v.y)
        
    def mostrar_vector(self):
        print("(",self.x,",",self.y,")",sep="")

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self,v):
        return self.x == v.x and self.y == v.y


v1 = Vector(5,4)
v2 = Vector(2,2)
v3 = Vector(-1,-1)
v = v1 + v2 + v3

u = v1 - v2   # se llama a v1.__sub__(v2)
w = Vector(3,2)

print("u:",u)
print("w:",w)

if u == w:  # se llama a u.__eq__(w)
    print("son iguales")
else:
    print("son distintos")
    
x = 1
y = 1

if x == y:
    print("son iguales")
else:
    print("son distintos")
    
