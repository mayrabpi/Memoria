class Jugador:
    def __init__(self,numero):
        self.numero = numero
        self.puntos=0

    def sumar_puntos(self):
        self.puntos+=1

    def obtener_puntos(self):
        return self.puntos
    

