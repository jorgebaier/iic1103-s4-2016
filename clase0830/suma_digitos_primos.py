import math

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma = suma + numero%10
        numero = numero // 10
    return suma


def esPrimo(n):
    i = 1
    divisores = 0
    while i <= n:
        if n%i == 0:
            divisores = divisores + 1
        i = i + 1
    return divisores == 2

def esPrimo2(n):
    i = 2
    if n < 2:
        return False
    while i < n:
        if n%i == 0:
            return False
        i = i + 1
    return True

def esPrimo3(n):
    i = 2
    if n < 2:
        return False
    while i <= math.sqrt(n):
        if n%i == 0:
            return False
        i = i + 1
    return True


def esPrimo4(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i <= math.sqrt(n):
        if n%i == 0:
            return False
        i = i + 2
    return True


limite = int(input("cuantos numeros quieres? "))
numero = 0
contador = 0
while contador < limite:
    suma = suma_digitos(numero)
    if esPrimo3(suma):
        print(numero)
        contador = contador + 1
    numero = numero + 1
