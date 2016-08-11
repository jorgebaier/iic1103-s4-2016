suma = 0

limite_inferior = int(input("limite inferior? "))
limite_superior = int(input("limite superior? "))

contador = limite_inferior

# calcula la suma entre 0 y limite

while contador < limite_superior + 1:
    suma =  suma + contador * contador
    contador = contador + 1

print("La suma de los cuadrados entre",limite_inferior,"y", limite_superior,"es", suma)




