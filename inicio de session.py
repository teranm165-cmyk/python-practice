usuario_corecto = "miguel"
contraseña_corecta = "miguel123"
mensaje_secreto = "hola miguel"

while True:
    print("\n---BIENVENIDO A INICIO DE SESSION---")
    print('1. iniciar session')
    print("2. salir")

    opcion = input("elige una opcion (1 o 2):")
    
    if opcion == "1":
            while True:
               usuario_ingresado = input("ingresse su usuario")
               contraseña_ingresada = input("ingrese su contraseña")
               if usuario_ingresado == usuario_corecto and contraseña_ingresada == contraseña_corecta:
                    print("\n bienvenido miguel la palabra secreta es:" , mensaje_secreto)
                    break
               else:
                    print("\n usuario o contraseñas incorectas. intenete de nuevo\n")

    elif opcion == "2":
         print('saliendo del programa')
         break
         


            


