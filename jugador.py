from cartas import *

class Jugador:
    def __init__(self, nombre,apuesta=0 ,mazo=list(), dinero=10000) :
        self.nombre = nombre
        self.apuesta = apuesta
        self.mazo = list()
        self.dinero = dinero

    dinero_inicial = 10000
