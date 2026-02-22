while True:

 import random

 opciones = ("piedra", "papel" , "tijera")

 jugador = input("elije papel , piedra o tijera")
 computadora = (opciones).lower()

 print("la computadora eligio ", computadora)


 if jugador == computadora ==:
    print("es un empate")
 

 elif jugador == "piedra" and computadora == "tijera":
    print("ganaste")  

 elif jugador == "tijera" and computadora == "papel":
    print("ganaste")

 elif jugador == "papel" and computadora == "piedra":
    print("ganaste") 

 else:
    print("perdiste")

 jugar_de_nuevo = input("quieres jugar otra vez (si/no): ") 

 if jugar_de_nuevo == "no":
   print("gracias por jugar")
   break