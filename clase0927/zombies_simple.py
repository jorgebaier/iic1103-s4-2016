

class Zombie:
    def __init__(self,nombre): # metodo "constructor" (inicializador)
                        # "crea"/"materializa" a un Zombie
        self.salud = 100 # salud es un atributo/propiedad
        self.color = 0   # el color del pelo es 0 por defecto
        self.nombre = nombre

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



z1 = Zombie("Lucas")
z2 = Zombie("Camila")
z1.imprimir()
z2.imprimir()
z2.tenir_pelo(1)
z1.imprimir()
z2.imprimir()
