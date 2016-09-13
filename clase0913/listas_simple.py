
cantidad = int(input("Cuantos numeros ingresaras: "))

i=0
lista=[]
while i < cantidad:
    numero = float(input("Ingresa el numero "+str(i+1)+": "))
    lista.append(numero)
    i = i + 1

suma = 0

for x in lista:
    suma = suma + x

promedio = suma / len(lista)

suma = 0
for x in lista:
    suma = suma + (x-promedio)**2
    
desviacion = suma / len(lista)

print("Promedio:",promedio)
print("Desviacion:",desviacion)


print(lista)

    
