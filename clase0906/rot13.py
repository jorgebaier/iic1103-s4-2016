def rotarLetra13(letra):
    if 'a' <= letra <= 'z':
        return chr( (ord(letra) - ord('a') + 13)%26 + ord('a'))
    if 'A' <= letra <= 'Z':
        return chr( (ord(letra) - ord('A') + 13)%26 + ord('A'))
    return letra

def rot13(mensaje):
    t=''
    for c in mensaje:
        t = t + rotarLetra13(c)
    return t

m = "Este es un Mensaje muy secreto"
m_secreto = rot13(m)
m_nosecreto = rot13(m_secreto)

print(m)
print(m_secreto)
print(m_nosecreto)
