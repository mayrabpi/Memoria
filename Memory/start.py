import os
class Start:
    def obtener_dimensiones():
        filas=int(input("Ingrese número de filas(2-6): "))
        columnas=int(input("Ingrese número de colimnas(2-5)"))
        return filas,columnas
    
    def limpiar_pantalla():
        os.system('cls'
                  if os.name == 'nt'
                  else 'clear')
        
    def pedir_carta(numero):
        fila=int(input(f"\nIngrese fila de la {numero} carta:"))
        col= int(input(f"Ingrese columna de la {numero} carta:"))
        return fila,col
