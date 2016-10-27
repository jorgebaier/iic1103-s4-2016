def suma_lista(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + suma_lista(L[1:])

def super_suma_lista(L):
    if len(L) == 0:
        return 0
    elif type(L[0]) == list:
        return super_suma_lista(L[0])+super_suma_lista(L[1:])
    else:
        return L[0]+super_suma_lista(L[1:])

def en(x,L):
    if len(L) == 0:
        return False
    elif L[0] == x:
        return True
    else:
        return en(x,L[1:])

def en2(x,L):
    if len(L) == 0:
        return False
    return L[0] == x or en2(x,L[1:])

    
print(suma_lista([1,2,3]))
print(suma_lista([1,2,3,4]))
print(super_suma_lista([[1,[[2],[[[[]]]]],[3,[1]],[[[4]]]]]))
#print(en(3,[1,2,3]))
#print(en(5,[1,2,3,4]))
