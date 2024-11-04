from jugador import Jugador
from tablero import Tablero
from start import Start
"""Clase que controla la lógica y el flujo del juego de memoria"""
class JuegoMemoria:
    """Inicializa un nuevo juego, configurando jugadores y tablero"""
    def __init__(self):
        filas, columnas = Start.obtener_dimensiones()
        self.tablero = Tablero(filas, columnas)
        self.jugador1 = Jugador(1)
        self.jugador2 = Jugador(2)
        self.total_pares = (filas * columnas) // 2
        self.pares_encontrados = 0
        self.turno_jugador = 1

    """Cambia el turno entre los jugadores"""
    def cambiar_turno(self):
        #self.turno_jugador = 2 if self.turno_jugador == 1 else 1
        if self.turno_jugador==1:
            self.turno_jugador=2
        else:
            self.turno_jugador=1
    
    """Obtiene el jugador que tiene el turno actual
       Retorna: Jugador: jugador actual"""
    def jugador_actual(self):
        return self.jugador1 if self.turno_jugador == 1 else self.jugador2
    
    """Muestra la puntuación actual de ambos jugadores y de quién es el turno """
    def mostrar_puntuacion(self):
        print(f"\nPuntos Jugador 1: {self.jugador1.obtener_puntos()}")
        print(f"Puntos Jugador 2: {self.jugador2.obtener_puntos()}")
        print(f"\nTurno del Jugador {self.turno_jugador}")
    
    """Muestra el resultado final del juego y declara al ganador"""
    def mostrar_resultado(self):
        print("\n¡Juego terminado!")
        print(f"Jugador 1: {self.jugador1.obtener_puntos()} puntos")
        print(f"Jugador 2: {self.jugador2.obtener_puntos()} puntos")
        
        if self.jugador1.obtener_puntos() > self.jugador2.obtener_puntos():
            print("¡Gana el Jugador 1!")
        elif self.jugador2.obtener_puntos() > self.jugador1.obtener_puntos():
            print("¡Gana el Jugador 2!")
        else:
            print("¡Empate!")

    def coordenda_valida(self,fila,columna):
        """Verifica si una coordenda está dentro de los límetes del tablero
            retorna True si la coordenada es valida, False en caso contrario"""
        if 0<=fila<self.tablero.filas and 0<=columna<self.tablero.columnas:
            return True
        else:
            return False
    
    def jugar(self):
        """Método principal que ejecuta el bucle del juego.
           Controla el flujo del juego hasta que se encuentren todas las parejas"""
        while self.pares_encontrados < self.total_pares:
            Start.limpiar_pantalla()
            self.mostrar_puntuacion()
            self.tablero.mostrar()
            
            # Primera carta
            while True:
              try:
                fila1, col1 = Start.pedir_carta("primera")
                if self.coordenda_valida(fila1,col1):
                  break
                else:
                  print("\nCoordenada inválida! Por favor, introduce una coordenada dentro del tablero ")
              except ValueError:
                  print("\n¡Error! Por favor introduce números válidos")
              except Exception:
                  print("\n¡Error! Tecla inválida")

              input("\nPresione Enter para continuar...")
              Start.limpiar_pantalla()
              self.tablero.mostrar()

            self.tablero.revelar_carta(fila1, col1)
            Start.limpiar_pantalla()
            self.tablero.mostrar()
            
            # Segunda carta
            while True:
              try:
                fila2, col2 = Start.pedir_carta("segunda")
                if self.coordenda_valida(fila2,col2):
                   break
                else:
                   print("\nCoordenada inválida! Por favor, introduce una coordenada dentro del tablero ")
              except ValueError:
                   print("\n¡Error! Por favor introduce números válidos")
              except Exception:
                   print("\n¡Error! Tecla inválida")
                   
              input("\nPresione Enter para continuar...")
              Start.limpiar_pantalla()
              self.tablero.mostrar()
                  
            self.tablero.revelar_carta(fila2, col2) 
            Start.limpiar_pantalla()
            self.tablero.mostrar()
            #Verificación de las cartas seleccionadas
            if self.tablero.son_iguales(fila1, col1, fila2, col2):
                print("\n¡Encontraste un par!")
                self.pares_encontrados += 1
                self.jugador_actual().sumar_puntos()
            else:
                print("\nNo son iguales")
                self.tablero.ocultar_carta(fila1, col1)
                self.tablero.ocultar_carta(fila2, col2)
                self.cambiar_turno()
            
            input("\nPresione Enter para continuar...")
        
        self.mostrar_resultado()