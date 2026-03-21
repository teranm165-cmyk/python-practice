jugadores = []

def agregar_jugador():
    nombre = input("escriba el nombre de juagdor")
    posicion = input("escriba su posicion")
    altura = input("escribe su altura")

    jugador = {
        "nombre":nombre,
        "posicion":posicion,
        "altura": altura
    }
    jugadores.append(jugador)
    print("jugador agregado exitosamente")

def mostrar_jugador():
    if len(jugadores) == 0:
        print("no hay jugadores")
        return
    for jugador in jugadores:
        print("nombre:", jugador["nombre"])
        print("posicion:", jugador["posicion"])
        print("------")

def buscar_jugadores():
    nombre_buscar = input("escriba el nombre por favor")
    for jugador in jugadores:
        if jugador["nombre"] == nombre_buscar:
            print("jugador encontrado")
            print("nombre:",jugador["nombre"])
            print("posicion:",jugador["posicion"])
            print("altura:",jugador["altura"])
            return
        else:
            print("jugador no encontrado")

while True:
    print("1. agregar jugador")
    print("2. mostrar jugador")
    print("3. buscar jugador")
    print("4. salir")

    opcion = input("eliga una opcion")

    if opcion == "1":
        agregar_jugador()

    elif opcion == "2":
        mostrar_jugador()

    elif opcion == "3":
        buscar_jugadores()

    elif opcion == "4":
        print("saliendo del programa")
        break
    else:
        print("opcion invalida")