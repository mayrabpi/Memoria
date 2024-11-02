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
