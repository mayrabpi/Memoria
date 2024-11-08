"""Clase que represnta a un jugador en el juego de memoria.
    Mantiene el resgitro de su número, nombre y puntuación"""

class Jugador:

    '''Inicializa un nuevo jugador.
       Argumento:
       numero(int):Número identificador del jugador'''
    def __init__(self,numero,nombre):
        self.numero = numero
        self.puntos=0
        self.parejas=0
        self.nombre=nombre

    """Método que incrementa la puntuación del jugador en 1 punto """
    def sumar_puntos(self):
        self.puntos+=2

    """Retorna la puntuación actual del jugador, return número de puntos del jufador """    
    def obtener_puntos(self):
        return self.puntos
    def suma_parejas(self):
        self.parejas+=1

    def obtener_parejas(self):
        return self.parejas
    
    def obtener_nombre(self):
        return self.nombre
    

