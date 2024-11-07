import os
from tablero import Tablero
"""Clase que maneja la configuración inicial y utilidades del juego"""
class Start:
   def mostrar_menu_principal():
       while True:
            print("\n----------Bienvenido al Juego de Memoria------------")
            print("\n1.Jugador vs Jugador")
            print("2.Jugador vs Máquina")
            print("3.Salir")
            try:
                opcion=int(input("\nSelccione una apción(1-2-3):"))
                if 1<=opcion<=3:
                    return opcion
                print("\n¡Error! Seleccione una opción válida(1-2-3):")
            except ValueError:
                print("\n¡Error! Seleccione un número válido")

            input("\nPresione Enter para continuar...")
            Start.limpiar_pantalla()

   """Solicita al usuario las dimenciones del tablero
      Retorna:tupla:Par de enteros(filas, columanas)"""         
   def obtener_dimensiones():
       def mostrar_menu():
           print("\n----------Configuración del Tablero------------")
           print()
           print("Tamaño mínimo: 2x2")
           print("Tamaño máximo: 6x5")
           print()

       mostrar_menu()
       while True:
           try:
               filas=int(input("Ingrese número de filas(2-6): "))
               columnas = int(input("Ingrese número de columnas (2-5): "))
               if filas<2 or filas>6 or columnas<2 or columnas>5:
                   print("\n¡Error! Las dimensiones deben estar entre 2x2 y 6x5")
               else:
                   total_casillas = filas*columnas
                   if total_casillas%2 !=0:
                       print("\n¡Error! El número total de casillas debe de ser para para formar parejas ")
                   else:
                       return filas,columnas
           except ValueError:
               print("\n¡Error! Por favor ingrse números enteros validos")

           input("Presione Enter para intentar de nuevo...")
           mostrar_menu
      
           
   

   """Limpia la pantalla de la consola"""
   def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')
  
   """Solicita las coordenadas de una carta
      Argumento: numero(str):Indicador de si es la primera o segunda carta
      Return:Par de enteros(fila,columna)"""
   def pedir_carta(numero):
        print()
        fila = int(input(f"Ingrese fila de la {numero} carta: "))-1
        col = int(input(f"Ingrese columna de la {numero} carta: "))-1
        return fila, col
   
   '''Metodo que obtiene los nombres de los jugadores ''' 
   def obtener_nombres():
       nombre1=input("Ingrese nombre del Jugador 1:")
       nombre2=input("Ingrese nombre del jugador 2:")
       return nombre1,nombre2
   
   '''Metodo que obtiene el nombre del jugador cuando elige jugar con la máquina'''
   def obtener_nombre_jugador():
       return input("Ingrese su nombre:")