
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma = suma + numero%10
        numero = numero // 10
    return suma


limite = int(input("cuantos numeros quieres? "))
numero = 0
contador = 0
while contador < limite:
    if suma_digitos(numero) == 8:
        print(numero)
        contador = contador + 1
    numero = numero + 1
