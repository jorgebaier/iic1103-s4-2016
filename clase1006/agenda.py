class Contacto:
    def __init__(self,nombre,email,direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_email(self):
        return self.email

    def __str__(self):
        s = "Nombre: "+self.nombre+"\n"
        s += "Email: "+self.email+"\n"
        s += "Direccion: "+self.direccion+"\n"
        return s
    
    def print_contacto(self):
        print("Nombre: ",self.nombre)
        print("Direccion: ",self.direccion)
        print("Email: ",self.email)

    def write(self,f):
        f.write(self.nombre+"\n")
        f.write(self.email+"\n")
        f.write(self.direccion+"\n")

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self,c):
        self.contactos.append(c)

    def print_contactos(self):
        for c in self.contactos:
            print(c)
            print()

    def buscar_contacto(self):
        clave = input('Qué quieres buscar? ')
        for c in self.contactos:
            if clave in c.get_nombre() or clave in c.get_email() or clave in c.get_direccion():
                c.print_contacto()

    def write(self,f):
        for c in self.contactos:
            c.write(f)
    


def input_contacto():
    nombre = input("Nombre del contacto:")
    email = input("Email del contacto:")
    direccion = input("Direccion del contacto:")
    return Contacto(nombre,email,direccion)

def print_menu():
    print("1. Crear Contacto")
    print("2. Buscar Contacto")
    print("3. Listar Contactos")
    print("4. Salir")


### 

a = Agenda()

f = open("datos.txt","r")
l = f.readlines()
f.close()

i = 0
while i < len(l):
    c = Contacto(l[i].strip(),l[i+1].strip(),l[i+2].strip())
    a.agregar_contacto(c)
    i = i + 3

while True:
    print_menu()
    opcion = input("Ingrese su opcion:")
    if opcion == "1":
        c = input_contacto()
        a.agregar_contacto(c)
    elif opcion == "2":
        print("Buscar Contacto:")
        a.buscar_contacto()
    elif opcion == "3":
        print("Lista de Contactos:")
        a.print_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

f = open("datos.txt","w")
a.write(f)
f.close()



