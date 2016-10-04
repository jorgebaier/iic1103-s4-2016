import random


class Universo:
    def __init__(self):
        self.plantas = []  # lista de plantas que contiene el universo
        self.zombies = []  # lista de zombies que contiene el universo

    def agregar_planta(self,planta):
        self.plantas.append(planta)

    def agregar_zombie(self,zombie):
        self.zombies.append(zombie)

    def cantidad_plantas(self):
        return len(self.plantas)

    def cantidad_zombies(self):
        return len(self.zombies)

    def print_stats(self):
        vidas_zombies = 0
        vidas_plantas = 0
        for z in self.zombies:
            vidas_zombies += z.get_salud()
        for p in self.plantas:
            vidas_plantas += p.get_salud()
        print("Plantas (",self.cantidad_plantas(),") = ",vidas_plantas,"Zombies (",self.cantidad_zombies(),") = ",vidas_zombies)

    def round_aleatorio(self):
        indice_planta = random.randint(0,self.cantidad_plantas()-1)
        indice_zombie = random.randint(0,self.cantidad_zombies()-1)
        p=self.plantas[indice_planta]
        z=self.zombies[indice_zombie]
        moneda = random.randint(0,1)
        if moneda == 0: # planta ataca a zombie
            z.recibe_ataque(p)
            if not z.esta_vivo():
                self.zombies.pop(indice_zombie)
        else:
            p.recibe_ataque(z)
            if not p.esta_viva():
                self.plantas.pop(indice_planta)
            

class Zombie:
    def __init__(self,nombre): # metodo "constructor" (inicializador)
                        # "crea"/"materializa" a un Zombie
        self.salud = 100 # salud es un atributo/propiedad
        self.color = 0   # el color del pelo es 0 por defecto
        self.nombre = nombre

    def get_color(self):
        return self.color

    def get_salud(self):
        return self.salud

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

    def get_salud(self):
        return self.salud

    def imprimir(self):
        print("Hola soy una planta. Me llamo",self.nombre,". Mi salud es:",self.salud)

    def esta_viva(self):
        return self.salud > 0
    
    def recibe_ataque(self,zombie):
        if zombie.get_color()==0:
            self.salud = self.salud - 10
        elif zombie.get_color()==1:
            self.salud = self.salud - 20
        else:
            self.salud = self.salud - 5


u = Universo()
i=0
while i<10:
    p = Planta("petunia "+str(i))
    u.agregar_planta(p)
    i = i + 1

i=0
while i<15:
    z = Zombie("michael "+str(i))
    u.agregar_zombie(z)
    i = i + 1

while u.cantidad_plantas() > 0 and u.cantidad_zombies() > 0:
    u.round_aleatorio()
    u.print_stats()
    
