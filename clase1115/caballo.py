N=6

def pretty_print(tablero):
    for fila in tablero:
        print(" ".join([str(x) for x in fila]))
        
def caballo(i,j,contador,tablero):
    if contador == N**2:
        pretty_print(tablero)
        return True
    deltas = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    for d in deltas:
        nuevo_i = i + d[0]
        nuevo_j = j + d[1]
        if 0 <= nuevo_i < N and 0 <= nuevo_j < N and tablero[nuevo_i][nuevo_j] == 0:
            tablero[nuevo_i][nuevo_j] = contador + 1
            if caballo(nuevo_i,nuevo_j,contador+1,tablero):
                return True
            tablero[nuevo_i][nuevo_j] = 0
    return False

tab = []
for i in range(N):
    tab.append([0]*N)

tab[0][0] = 1
caballo(0,0,1,tab)
