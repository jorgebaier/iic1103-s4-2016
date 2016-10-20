def selection_sort(L):
    i = 0
    while i < len(L) - 1:
        minimo = L[i]
        indice_minimo = i
        j = i + 1
        while j < len(L): # busca el elemento más pequeño en L[i:]
            if L[j] < minimo:
                minimo = L[j]
                indice_minimo = j
            j += 1
        L[indice_minimo] = L[i]
        L[i] = minimo
        i += 1


nombre = input("Nombre del archivo: ")
f = open(nombre, "r")
L = [int(linea.strip()) for linea in f.readlines()]
f.close()

selection_sort(L)

for x in L:
    print(x, end=' ')


