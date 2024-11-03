import random
"""Clase que representa el tablero del juego.
   Maneja la creación,visualización y manipulación del tablero"""
class Tablero:
     """Inicializa un nuevo tablero.
         Argumentos:
         filas(int):Número de filas del tablero
         columnas(int):Número de columnas del tablero"""
     def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self._crear_tablero()
        self.tablero_visible = self._crear_tablero_visible()


     """Crea el tablero con pares de símbolos distribuidos aleatoriamente.
         Retorna:Matriz que representa el tablero con los símbolos""" 
     def _crear_tablero(self):
        simbolos = ["🌟","🌈","🌸","🍀","🎮","🎨","🎭","🎪","🦋","🐬","🐶","🐱","🦁","🐯","🦊","🦝"]#Lista de simbolos
        simbolos = simbolos[:(self.filas * self.columnas) // 2]#toma solo los símbolos necesarios según el tamaño del tablero
        simbolos = simbolos * 2#Duplica los símbolos para crear pares
        random.shuffle(simbolos)#Mezcla los símbolos aleatorimente
        
        tablero = []#crea la matriz del tablero
        posicion = 0
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(simbolos[posicion])
                posicion += 1
            tablero.append(fila)
        return tablero
     
    
     """Crea el tablero que se muestra al jugador, inicialmente con los elementos ocultos
        Retorna: List: Matriz que representa el tablero visible con '*' en todas las posiciones"""    
     def _crear_tablero_visible(self):
        return [['*' for j in range(self.columnas)] for i in range(self.filas)]
     

     """Muestra el estado actual del tablero en la consala."""
     def mostrar(self):
         #Muestra los números de la columnas
        print("  ", end="")
        for j in range(self.columnas):
            print(f" {j}", end="")
        print()
        #Muestra las filas con sus números
        for i in range(self.filas):
            print(f"{i}", end=" ")
            for j in range(self.columnas):
                print(f" {self.tablero_visible[i][j]}", end="")
            print()


     """Revela una carta en la posición especicada
        Argumentos:
        filas(int):número de fila de la carta
        columna(int):número de colimnas de la carta
        Retorna: str:Símbolo de la carta revelada"""      
     def revelar_carta(self, fila, columna):
        self.tablero_visible[fila][columna] = self.tablero[fila][columna]
        return self.tablero[fila][columna]
     
     """Oculta una carta en la posición especicada
        Argumentos:
        fila(int):Número de filas de la carta
        columna(int):Número de columnas de la carta"""   
     def ocultar_carta(self, fila, columna):
        self.tablero_visible[fila][columna] = '*'
        

     """Verifica s dos cartas son iguales
        Argumentos:
        fila1(int):Fila de la primera carta
        col1(int):columna de la primera carta
        fila2(int):Fila de la segunda carta
        col2(int):columna de la segunda carta"""
     def son_iguales(self, fila1, col1, fila2, col2):
        return self.tablero[fila1][col1] == self.tablero[fila2][col2]
