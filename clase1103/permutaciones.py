
# insertar(a,s) retorna una lista que contiene todos los
# strings que resultan de insertar a en alguna
# ubicación de s

def insertar(a,s): 
    return [s[:i] + a + s[i:] for i in range(len(s)+1)]

def perm(s):
    if s == '':
        return ['']
    else:
        L=[]
        for t in perm(s[1:]):
            L.extend(insertar(s[0],t))
        return L
print(perm('abcdfg'))
#print(perm('abcd'))
