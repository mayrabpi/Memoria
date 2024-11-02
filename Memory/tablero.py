import random
class tablero:
    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas=columnas
        self.tablero = self.crear_tablero()
        self.tablero_visible = self.crear_tablero_visible()

    def crear_tablero(self):
        simbolos=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        simbolos=simbolos[:(self.filas*self.columnas)//2]
        simbolos = simbolos*2
        random.shufle(simbolos)

        tablero=[]
        posicion=0
        for i in range(self.filas):
            fila=[]
            for j in range(self.columnas):
                fila.append(simbolos[posicion])
                posicion+=1
            tablero.append(fila)
            return tablero
