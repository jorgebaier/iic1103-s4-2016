
# mezcla(L1,L2), suponiendo que L1 y L2 están ordenadas,
# retorna una lista ordenada con los elementos de L1 y L2
def mezcla(L1,L2):
    i = j = 0
    R = []
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
            j += 1

    if i >= len(L1):
        R.extend(L2[j:])
    if j >= len(L2):
        R.extend(L1[i:])
    return R


def mergesort(L):
    if len(L) <= 1:
        return L
    mitad = len(L)//2
    L1 = mergesort(L[:mitad])
    L2 = mergesort(L[mitad:])
    return mezcla(L1,L2)

nombre = input("Nombre del archivo: ")
f = open(nombre, "r")
L = [int(linea.strip()) for linea in f.readlines()]
f.close()

L=mergesort(L)

for x in L:
    print(x, end=' ')


