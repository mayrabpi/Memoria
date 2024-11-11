from jugador import Jugador
from tablero import Tablero
from start import Start
import random
"""Clase que controla la lógica y el flujo del juego de memoria"""
class JuegoMemoria:
    """Inicializa un nuevo juego, configurando jugadores y tablero"""
    def __init__(self, modo_juego):
        self.modo_juego=modo_juego
        filas, columnas = Start.obtener_dimensiones()
        self.tablero = Tablero(filas, columnas)
        
        if self.modo_juego==1:#jugador vs jugador
            nombre1,nombre2=Start.obtener_nombres()
            self.jugador1 = Jugador(1,nombre1)
            self.jugador2 = Jugador(2,nombre2)
        elif self.modo_juego==2: #jugador vs máquina
            nombre=Start.obtener_nombre_jugador()
            self.jugador1=Jugador(1,nombre)
            self.jugador2=Jugador(2,"Máquina")
        else:#maquina vs maquina
            self.jugador1=Jugador(1,"Máquina1")
            self.jugador2=Jugador(2,"Máquina2")



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
        print(f"\nPuntos {self.jugador1.obtener_nombre()}: {self.jugador1.obtener_puntos()}")
        print(f"Puntos {self.jugador2.obtener_nombre()}: {self.jugador2.obtener_puntos()}")
        print(f"\nTurno de {self.jugador_actual().obtener_nombre()}")
    
    """Muestra el resultado final del juego y declara al ganador"""
    def mostrar_resultado(self):
        print("\n¡Juego terminado!")
        print(f"{self.jugador1.obtener_nombre()}: {self.jugador1.obtener_puntos()} puntos")
        print(f"{self.jugador2.obtener_nombre()}: {self.jugador2.obtener_puntos()} puntos")
        
        if self.jugador1.obtener_puntos() > self.jugador2.obtener_puntos():
            print(f"¡Gana {self.jugador1.obtener_nombre()} !,has encontrado {self.jugador1.obtener_parejas()} parejas")
        elif self.jugador2.obtener_puntos() > self.jugador1.obtener_puntos():
            print(f"¡Gana {self.jugador2.obtener_nombre()} !,has encontrado {self.jugador2.obtener_parejas()} parejas")
        else:
            print("¡Empate!")

    def coordenda_valida(self,fila,columna):
        """Verifica si una coordenda está dentro de los límetes del tablero
            retorna True si la coordenada es valida, False en caso contrario"""
        if 0<=fila<self.tablero.filas and 0<=columna<self.tablero.columnas:
            return True
        else:
            return False
    '''Método que simula el turno de la máquina'''    
    def turno_maquina(self):
       jugador_actual= self.jugador_actual()
       print(f"\nTurno de {jugador_actual.obtener_nombre()}")
       input("Presione Enter para continuar...")
        
        # Primera carta
       while True:
            fila1 = random.randint(0, self.tablero.filas - 1)
            col1 = random.randint(0, self.tablero.columnas - 1)
            if not self.tablero.esta_revelada(fila1, col1):
                break
        
       self.tablero.revelar_carta(fila1, col1)
       Start.limpiar_pantalla()
       self.tablero.mostrar()
       print(f"\n {jugador_actual.obtener_nombre()} elige la posición [{fila1+1}, {col1+1}]")
       input("\nPresione Enter para continuar...")
        
        # Segunda carta
       while True:
            fila2 = random.randint(0, self.tablero.filas - 1)
            col2 = random.randint(0, self.tablero.columnas - 1)
            if not self.tablero.esta_revelada(fila2, col2) and (fila2 != fila1 or col2 != col1):
                break
        
       self.tablero.revelar_carta(fila2, col2)
       Start.limpiar_pantalla()
       self.tablero.mostrar()
       print(f"\n{jugador_actual.obtener_nombre()} elige la posición [{fila2+1}, {col2+1}]")
       input("\nPresione Enter para continuar...")
        #verificar si las cartas son iguales
       if self.tablero.son_iguales(fila1,col1,fila2,col2):
           print(f"\n {jugador_actual.obtener_nombre()} encontro un par")
           self.pares_encontrados+=1
           self.jugador2.sumar_puntos()
           self.jugador2.suma_parejas()
       else:
           print(f"\n {jugador_actual.obtener_nombre()} no encontro un par")
           input("\nPresione enter para continuar")
           self.tablero.ocultar_carta(fila1,col1)
           self.tablero.ocultar_carta(fila2,col2)
           self.cambiar_turno()

    def jugar(self):
        
        """Método principal que ejecuta el bucle del juego.
           Controla el flujo del juego hasta que se encuentren todas las parejas"""
        while self.pares_encontrados < self.total_pares:
            Start.limpiar_pantalla()
            self.mostrar_puntuacion()
            self.tablero.mostrar()
            if self.modo_juego == 3 or (self.modo_juego == 2 and self.turno_jugador == 2):
                self.turno_maquina()
            else:#turno jugador
            # Primera carta
              while True:
                try:
                  fila1, col1 = Start.pedir_carta("primera")
                  if not self.coordenda_valida(fila1,col1):
                    print("\nCoordenada inválida! Por favor, introduce una coordenada dentro del tablero ")
                  elif self.tablero.esta_revelada(fila1,col1):
                    print("\n!Esta carta ya está revelada! Elige otra carta") 
                  else:
                    break    
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
                  if not self.coordenda_valida(fila2,col2):
                      print("\nCoordenada inválida! Por favor, introduce una coordenada dentro del tablero ")
                  elif self.tablero.esta_revelada(fila2,col2):
                      print("\n!Esta carta ya está revelada! Elige otra carta") 
                  else:
                     break
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
                  self.jugador_actual().suma_parejas()
              else:
                  print("\nNo son iguales")
                  self.tablero.ocultar_carta(fila1, col1)
                  self.tablero.ocultar_carta(fila2, col2)
                  self.cambiar_turno()
              if self.pares_encontrados < self.total_pares:
            
               input("\nPresione Enter para continuar...")
        
        self.mostrar_resultado()