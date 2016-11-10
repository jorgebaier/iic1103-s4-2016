def encuentra_suma(lista,valor):
    if lista==[]:
        return valor == 0
    if encuentra_suma(lista[1:],valor-lista[0]):
        return True
    if encuentra_suma(lista[1:],valor):
        return True
    return False

def muestra_suma(lista,valor,sol):
    if lista==[]:
        if valor == 0:
            print(sol)
            return True
        else:
            return False
    if muestra_suma(lista[1:],valor-lista[0],sol+[lista[0]]):
        return True
    if muestra_suma(lista[1:],valor,sol):
        return True
    return False

def muestra_todas(lista,valor,sol):
    if lista==[]:
        if valor == 0:
            print(sol)
            return False
        else:
            return False
    if muestra_todas(lista[1:],valor-lista[0],sol+[lista[0]]):
        return True
    if muestra_todas(lista[1:],valor,sol):
        return True
    return False

#print(encuentra_suma([4,10,9,3,11],7))
#print(encuentra_suma([4,10,9,3,11],22))
#print(encuentra_suma([4,10,9,3,11],24))
#print(encuentra_suma([4,10,9,3,11],220))
#print(encuentra_suma([4,10,9,3,11],-8))

#print(muestra_suma([4,10,9,3,11],7,[]))
#print(muestra_suma([4,10,9,3,11],22,[]))
#print(muestra_suma([4,10,9,3,11],24,[]))
#print(muestra_suma([4,10,9,3,11],220,[]))
#print(muestra_suma([4,10,9,3,11],-8,[]))

print(muestra_todas([4,10,9,3,11],7,[]))
print(muestra_todas([4,10,9,3,11],22,[]))
print(muestra_todas([4,10,9,3,11],24,[]))
print(muestra_todas([4,10,9,3,11],220,[]))
print(muestra_todas([4,10,9,3,11],-8,[]))
