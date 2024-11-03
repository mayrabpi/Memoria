import os
"""Clase que maneja la configuración inicial y utilidades del juego"""
class Start:

   """Solicita al usuario las dimenciones del tablero
      Retorna:tupla:Par de enteros(filas, columanas)"""
   def obtener_dimensiones():
        print("\n----------Bienvenido al Juego de Memoria------------")
        print()
        print("Tamaño mínimo: 2x2")
        print("Tamaño máximo: 6x5")
        print()
      
        filas = int(input("Ingrese número de filas (2-6): "))
        columnas = int(input("Ingrese número de columnas (2-5): "))
        return filas, columnas

   """Limpia la pantalla de la consola"""
   def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')
  
   """Solicita las coordenadas de una carta
      Argumento: numero(str):Indicador de si es la primera o segunda carta
      Return:Par de enteros(fila,columna)"""
   def pedir_carta(numero):
        fila = int(input(f"Ingrese fila de la {numero} carta: "))
        col = int(input(f"Ingrese columna de la {numero} carta: "))
        return fila, col