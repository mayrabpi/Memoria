import random

def crear_tablero(filas, columnas):
    # Lista de símbolos que usaremos (letras)
    simbolos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    # Tomamos solo los símbolos necesarios y los duplicamos para hacer pares
    simbolos = simbolos[:(filas * columnas) // 2] * 2
    # Mezclamos los símbolos
    random.shuffle(simbolos)
    
    # Creamos el tablero con los símbolos
    tablero = []
    posicion = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(simbolos[posicion])
            posicion += 1
        tablero.append(fila)
    
    return tablero

def mostrar_tablero_oculto(filas, columnas):
    print("\nTablero Oculto:")
    print("  ", end="")
    # Mostrar números de columnas
    for j in range(columnas):
        print(f" {j}", end="")
    print()
    
    # Mostrar filas con asteriscos
    for i in range(filas):
        print(f"{i}", end=" ")
        for j in range(columnas):
            print(" *", end="")
        print()

def mostrar_tablero_visible(tablero):
    print("\nTablero con elementos:")
    print("  ", end="")
    # Mostrar números de columnas
    for j in range(len(tablero[0])):
        print(f" {j}", end="")
    print()
    
    # Mostrar filas con símbolos
    for i in range(len(tablero)):
        print(f"{i}", end=" ")
        for j in range(len(tablero[0])):
            print(f" {tablero[i][j]}", end="")
        print()

# Programa principal
filas = int(input("Ingrese número de filas (2-6): "))
columnas = int(input("Ingrese número de columnas (2-5): "))

# Crear y mostrar los tableros
tablero = crear_tablero(filas, columnas)
mostrar_tablero_oculto(filas, columnas)
mostrar_tablero_visible(tablero)
