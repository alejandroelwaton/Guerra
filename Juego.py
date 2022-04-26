from jugador import *
import pickle, random, os

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores

    def cargar():
            """Esta funcion carga los datos
            """
            jugadores_db = open('jugadores.pickle', 'rb')
            db = pickle.load(jugadores_db)
            jugadores_db.close()
            return db

    def ganador(self):
        self.juga
  
    def guardar(db):
            with open('jugadores.pickle', 'wb')as file :
                pickle.dump(db,file)

    def jugar(self):
        self.cargar()
        self.jugadores = self.cargar()

        if len(self.jugadores) >=2:
            mazo = Mazo()
            mazo = mazo.cartas_organizadas
            i = 0
            while len(mazo)> 1 :
                carta = mazo.pop(random.randint(0,len(mazo)-1))
                self.jugadores[i%len(self.jugadores)].mazo.append(carta)
                i += 1
            for jugador in self.jugadores:
                print(jugador.nombre,":",jugador.mazo)
                print(
'''


''')
        #print(f'El jugador {db.index(jugador)}. {jugador.nombre} Saco la carta {}')
    def menu_principal(self):
        while True: 
            print()
            for jugadores in db:
                self.cargar()
                print(f'{db.index(jugadores)+1}. {jugadores.nombre}, Su dinero es: {jugadores.dinero}')

            while len(db) > 4:
                for jugadores in db:
                   print(db.index(jugadores)+1,'.', jugadores.nombre)
                eliminar = int(input(f'Hay mas de {len(db)} jugadores en el juego, elimine el jugador/jugadores que desea eliminar: ')) 
                db.pop(eliminar -1)
                self.guardar(db)
                print('Los jugadores serian: ')       
                for jugadores in db:
                    print(db.index(jugadores)+1,'.', jugadores.nombre)

            opcion = int(input("""
            menu 
    1. Agregar Jugador
    2. Borrar Jugador 
    presione cualquier numero(menos 1,2)para entrar al juego
                """))
            if opcion ==1:
                if True:
                    jugadores = int(input("Cuantas Personas Van a Jugar?:"))#aqui le preguntamos al usuario la cantidad de jugadores a agregar
                    while jugadores <1 or jugadores >4:#con este if podemos ponerle el limite de jugadores que sea de 2-4
                        print('cantidad de jugadores no validos')
                        jugadores = int(input("Cuantas Personas Van a Jugar?:"))#aqui le preguntamos al usuario la cantidad de jugadores a agregar
                print (jugadores)
                for k in range (jugadores):
                    nombre = str (input(f'ingrese nombre del jugador{k+1}: '))
                    apuesta = int(input(f'Cuanto va a apostar el jugador {k+1}: '))
                    while apuesta > Jugador.dinero_inicial:
                        apuesta= int(input(f'No puedes apostar mas de {Jugador.dinero_inicial}, apuesta una cantidad valida: '))
                    jugador =Jugador(nombre, apuesta, [], 10000 - apuesta)
                    db.append (jugador)
                    self.guardar(db)

            elif opcion == 2:
                self.cargar()
                i =int(input('Numero del jugador que deseas eliminar: '))
                db.pop(i-1)
                while len(db) >= 1:
                    print('no puedes hacer menos de un jugador')
                    Juego.menu_principal(Juego)
                for a in db:
                    print(f"Los usuarios serian = {a.nombre}")
                self.guardar(db)

            else:
                print(f'Van a jugar Guerra' )
                self.jugar(self)
                break



    

db = Juego.cargar()


