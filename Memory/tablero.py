import random
class Tablero:
     def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self._crear_tablero()
        self.tablero_visible = self._crear_tablero_visible()
        
     def _crear_tablero(self):
        simbolos = ["🌟","🌈","🌸","🍀","🎮","🎨","🎭","🎪","🦋","🐬","🐶","🐱","🦁","🐯","🦊","🦝"]
        simbolos = simbolos[:(self.filas * self.columnas) // 2]
        simbolos = simbolos * 2
        random.shuffle(simbolos)
        
        tablero = []
        posicion = 0
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(simbolos[posicion])
                posicion += 1
            tablero.append(fila)
        return tablero
    
     def _crear_tablero_visible(self):
        return [['*' for j in range(self.columnas)] for i in range(self.filas)]
    
     def mostrar(self):
        print("  ", end="")
        for j in range(self.columnas):
            print(f" {j}", end="")
        print()
        
        for i in range(self.filas):
            print(f"{i}", end=" ")
            for j in range(self.columnas):
                print(f" {self.tablero_visible[i][j]}", end="")
            print()
            
     def revelar_carta(self, fila, columna):
        self.tablero_visible[fila][columna] = self.tablero[fila][columna]
        return self.tablero[fila][columna]
    
     def ocultar_carta(self, fila, columna):
        self.tablero_visible[fila][columna] = '*'
        
     def son_iguales(self, fila1, col1, fila2, col2):
        return self.tablero[fila1][col1] == self.tablero[fila2][col2]
