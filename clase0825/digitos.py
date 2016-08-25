
numero = 1948

cifras = 0
while numero // 10**cifras != 0:
    cifras = cifras + 1

suma = 0

i = 1
while i <= cifras:
    suma = suma + (numero // 10**(i-1))%10
    i = i + 1


suma2 = 0
while numero > 0:
    suma2 = suma2 + numero%10
    numero = numero // 10

print("las cifras del numero segun metodo 1 suman",suma)
print("las cifras del numero segun metodo 2 suman",suma2)
