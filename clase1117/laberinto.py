import os
import time
class Vector:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __add__(self,v):
		return Vector(self.x+v.x,self.y+v.y)

	def __eq__(self,v):
		return self.x==v.x and self.y==v.y

	def __str__(self):
		return "(" + str(self.x) + ","+ str(self.y) + ")"

class Laberinto:

	def __init__(self, path):
		self.cargar_archivo(path)
		self.posicion_robot()
		self.visitados=[]


	def imprimir(self):
		for fila in self.lab:
			print(''.join(fila))


	def cargar_archivo(self, path):
		archivo = open(path)
		self.lab = []
		for linea in archivo:
			lab_linea = []
			for c in linea.rstrip('\n'):
				lab_linea.append(c)
			self.lab.append(lab_linea)
		archivo.close()

	def posicion_robot(self):
		for i in range(len(self.lab)):
			for j in range(len(self.lab[i])):
				if self.lab[i][j] == '+':
					self.pos = Vector(i,j)


        # retorna las movidas posibles del robot
	def movidas_posibles(self):
		desp=[Vector(-1,0),Vector(1,0),Vector(0,-1),Vector(0,1)]
		movs=[]
		for d in desp:
			nueva_pos=self.pos+d
			if self.lab[nueva_pos.x][nueva_pos.y]!='x' and not nueva_pos in self.visitados:
				movs.append(nueva_pos)
		return movs

        # muestra lentamente el avance del robot en la pantalla
	def marcar_ruta(self):
		for v in self.visitados:
			os.system('clear')
			if self.lab[v.x][v.y]!='g':
				self.lab[v.x][v.y]='*'
			self.imprimir()
			time.sleep(0.3)

def resolver(laberinto):
        if laberinto.lab[laberinto.pos.x][laberinto.pos.y]=='o':
                laberinto.marcar_ruta()
                return True
        movs = laberinto.movidas_posibles()
        for m in movs:
                if m not in laberinto.visitados:
                        posicion_antigua = laberinto.pos
                        laberinto.pos = m
                        laberinto.visitados.append(m)
                        if resolver(laberinto):
                                return True
                        laberinto.visitados.pop()
                        laberinto.pos = posicion_antigua
        return False

def resolver_optimo(laberinto,i,maximo):
        if i>maximo:
                return False
        if laberinto.lab[laberinto.pos.x][laberinto.pos.y]=='o':
                laberinto.marcar_ruta()
                return True
        movs = laberinto.movidas_posibles()
        for m in movs:
                if m not in laberinto.visitados:
                        posicion_antigua = laberinto.pos
                        laberinto.pos = m
                        laberinto.visitados.append(m)
                        if resolver_optimo(laberinto,i+1,maximo):
                                return True
                        laberinto.visitados.pop()
                        laberinto.pos = posicion_antigua
        return False



# Código principal
lab = Laberinto('maze_3.txt')
lab.imprimir()
for limite in range(1,10000):
        if resolver_optimo(lab,0,limite):
                break
        
	
