from random import sample
class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor 
        self.pinta = pinta
    
    def __repr__(self):
        return f'{self.valor}{self.pinta}'

    def mostrar(self):
        print(f'{self.valor}{self.pinta}')

class Mazo() :
    def __init__(self):
        self.valores = ['As'] + [str (x) for x in range(2,11)]+ ['J', 'Q', 'K']
        self.pintas = ['♠️', '♣️', '♦️', '♥️']
        self.cartas_organizadas = self.crear_cartas()
        self.cartas = self.revolver()

    def crear_cartas (self):
        cartas_organizadas =[Carta(valor,pinta) for valor in self.valores for pinta in self.pintas ]
        return  cartas_organizadas

    def mostrar (self):
        print (f'en el mazo hay {len(self.cartas_organizadas)}casrtas')
        for carta in self.cartas_organizadas:
            carta.mostrar()

    def revolver (self):
        return sample(self.cartas_organizadas, len(self.cartas_organizadas))
if __name__ == '__main__':
    x=Mazo()
    x.mostrar()
