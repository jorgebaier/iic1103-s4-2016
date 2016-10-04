
nombre = input("Que archivo quieres leer")

f = open(nombre,"r")

for linea in f:
    linea = linea.strip()
    print(linea)

f.close()
