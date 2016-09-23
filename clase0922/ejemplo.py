import bigramas_ord

# bigramas_ord.cargar_archivo() : carga archivo de datos
# bigramas_ord.palabra_comun_seguida(palabra):
#   retorna una palabra que ocurre frecuentemente despues
#   de palabra

def leer_prohibidas():
    # retorna un string que contiene las letras prohibidas
    print('qué letras quieres omitir? ')
    s = ''
    c = ''
    while c != '0':
        s = s + c
        c = input()
    return s

def legal(prohibidas,palabra):
    # retorna True si la palabra no contiene
    # ningun caracter en prohibidas
    # retorna False en caso contrario
    for c in prohibidas:
        if c in palabra:
            return False
    return True



bigramas_ord.cargar_archivo()

cuantas_palabras = int(input('cuantas palabras quieres? '))
palabra_inicial = input('palabra inicial? ')
prohibidas = leer_prohibidas()

print("Letras prohibidas:",prohibidas)

contador = 0

palabra = palabra_inicial
while contador < cuantas_palabras:
    print(palabra, end=' ')
    palabra_original = palabra
    palabra = bigramas_ord.palabra_comun_seguida(palabra_original)
    while not legal(prohibidas,palabra):
        palabra = bigramas_ord.palabra_comun_seguida(palabra_original)    
    contador += 1 # contador = contador + 1

