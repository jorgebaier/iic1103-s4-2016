
def substring(s1,s2):
    # retorna True si s1 está contenido en s2
    i = 0
    while i <= len(s2) - len(s1):
        if s2[i:len(s1)+i] == s1:
            return True
        i = i + 1

s1="a-b"
s2="arb"


s1="c-b"

def iguales_guion(s1,s2):
    i = 0
    while i < len(s1):
        if s1[i] != s2[i] and s1[i] != '-':
            return False
        if s1[i] == '-' and (s2[i] < 'a' or s2[i] > 'z'):
            return False
        i = i + 1
    return True


def substring_guion(s1,s2):
    # retorna True si s1 está contenido en s2
    i = 0
    while i <= len(s2) - len(s1):
        if iguales_guion(s1,s2[i:len(s1)+i]):
            return True
        i = i + 1
