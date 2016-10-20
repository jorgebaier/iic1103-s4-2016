import time
import random

def buscar(n,L): #retorna True si n está en L
                 #retorna False en otro caso
    for x in L:
        if x == n:
            return True
        if x > n:
            return False
    return False

def busqueda_binaria(n,L):
    inicio = 0
    fin = len(L) - 1
    while inicio <= fin:
        mitad = (inicio + fin)//2
        if L[mitad] == n:
            return True
        elif L[mitad] > n:
            fin = mitad - 1
        else:
            inicio = mitad + 1
    return False

n = 0
L = []

tic1=time.time()

for i in range(0,10000000):
    L.append(n)
    delta = random.randint(0,100)
    n += delta
    
tic2=time.time()

print("Datos generados en ",round(tic2-tic1,2)," segundos.")

print(L[-1])



while True:
    numero = int(input("Que numero buscas? "))

    tic1=time.time()

    if buscar(numero,L):
        print("Lo encontré!!")
    else:
        print("no está :(")
    
    tic2=time.time()
    print("Busqueda lineal se completó en ",round(tic2-tic1,2)," segundos.")

    tic1=time.time()

    if busqueda_binaria(numero,L):
        print("Lo encontré!!")
    else:
        print("no está :(")
    
    tic2=time.time()
    print("Busqueda binaria se completó en ",round(tic2-tic1,2)," segundos.")

