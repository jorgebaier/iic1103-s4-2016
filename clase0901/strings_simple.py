

s = "esto es un string"

i = 0

#while i < len(s):
#    print(s[i])
#    i = i + 1

#for a in s:
#    print(a)


st = ""

for a in s:
    if a != " ":
        st = st + a
    else:
        st = st + "\n"

print(st)
