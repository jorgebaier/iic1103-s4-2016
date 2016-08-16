suma = 0

limite_inferior = int(input("limite inferior? "))
limite_superior = int(input("limite superior? "))



if limite_superior < limite_inferior:
    print("El limite superior no puede ser menor que el inferior")
else:    
    contador = limite_inferior

    # calcula la suma entre 0 y limite

    while contador < limite_superior + 1:
        decenas = (contador // 10) % 10
        unidades = contador % 10
        if  decenas == 2 or unidades % 4==0:
            suma =  suma + contador
        contador = contador + 1

    print("La suma entre",limite_inferior,"y", limite_superior,"es", suma)




