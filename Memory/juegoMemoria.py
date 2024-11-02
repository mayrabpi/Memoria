from jugador import Jugador
from tablero import Tablero
from start import Start
class JuegoMemoria:
    def __init__(self):
        filas, columnas = Start.obtener_dimensiones()
        self.tablero = Tablero(filas, columnas)
        self.jugador1 = Jugador(1)
        self.jugador2 = Jugador(2)
        self.total_pares = (filas * columnas) // 2
        self.pares_encontrados = 0
        self.turno_jugador = 1
    
    def cambiar_turno(self):
        self.turno_jugador = 2 if self.turno_jugador == 1 else 1
    
    def jugador_actual(self):
        return self.jugador1 if self.turno_jugador == 1 else self.jugador2
    
    def mostrar_puntuacion(self):
        print(f"\nPuntos Jugador 1: {self.jugador1.obtener_puntos()}")
        print(f"Puntos Jugador 2: {self.jugador2.obtener_puntos()}")
        print(f"\nTurno del Jugador {self.turno_jugador}")
    
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
    
    def jugar(self):
        while self.pares_encontrados < self.total_pares:
            Start.limpiar_pantalla()
            self.mostrar_puntuacion()
            self.tablero.mostrar()
            
            # Primera carta
            fila1, col1 = Start.pedir_carta("primera")
            self.tablero.revelar_carta(fila1, col1)
            
            Start.limpiar_pantalla()
            self.tablero.mostrar()
            
            # Segunda carta
            fila2, col2 = Start.pedir_carta("segunda")
            self.tablero.revelar_carta(fila2, col2)
            
            Start.limpiar_pantalla()
            self.tablero.mostrar()
            
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