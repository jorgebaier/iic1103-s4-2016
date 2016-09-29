

class Zombie:
    def __init__(self,nombre): # metodo "constructor" (inicializador)
                        # "crea"/"materializa" a un Zombie
        self.salud = 100 # salud es un atributo/propiedad
        self.color = 0   # el color del pelo es 0 por defecto
        self.nombre = nombre

    def get_color(self):
        return self.color

    def tenir_pelo(self, nuevo_color):
        self.color = nuevo_color

    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            return False

    def imprimir(self):
        if self.color==0:
            str_color = "negro"
        elif self.color==1:
            str_color = "amarillo"
        elif self.color==2:
            str_color = "rojo"
        elif self.color==3:
            str_color = "morado"
        else:
            str_color = "blanco"

        if self.esta_vivo:
            str_vivo = "Estoy vivo"
        else:
            str_vivo = "Estoy MUERTO"

        print("Soy un zombie.",str_vivo,". Me llamo",self.nombre,". Mi salud es:",self.salud,"y el color de mi pelo es", str_color)

    def recibe_ataque(self,planta):
        self.salud = self.salud - 15

class Planta:
    def __init__(self,nombre):
        self.salud  = 100
        self.nombre = nombre

    def imprimir(self):
        print("Hola soy una planta. Me llamo",self.nombre,". Mi salud es:",self.salud)

    def recibe_ataque(self,zombie):
        if zombie.get_color()==0:
            self.salud = self.salud - 10
        elif zombie.get_color()==1:
            self.salud = self.salud - 20
        else:
            self.salud = self.salud - 5
            

z2 = Zombie("Camila")
z2.tenir_pelo(1)

p1 = Planta("Camelia")

z2.imprimir()
p1.imprimir()

z2.recibe_ataque(p1)  # Camelia ataca a Camila

print()

z2.imprimir()
p1.imprimir()


p1.recibe_ataque(z2)# Camila ataca a Camelia

z2.imprimir()
p1.imprimir()

