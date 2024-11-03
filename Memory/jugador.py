class Jugador:
    """Clase que represnta a un jugador en el juego de memoria.
    Mantiene el resgitro de su número, nombre y puntuación"""
    def __init__(self,numero):
        self.numero = numero
        self.puntos=0

    def sumar_puntos(self):
        self.puntos+=1

    def obtener_puntos(self):
        return self.puntos
    

