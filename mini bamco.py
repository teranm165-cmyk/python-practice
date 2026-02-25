saldo = 0
cuenta_creada = False

while True:
    print("\n---BIENVENIDO A TU MII BANCO---")
    print("1. crear cuenta")
    print("2. ver saldo")
    print("3. depositar")
    print("4. retirar")
    print("5. salir")

    opcion = input("selecciona una opcion")

    if opcion == "1":
        if not cuenta_creada:
            saldo = 0
            cuenta_creada = True
            print("cuenta creada con exito")
        else:
            print("la cuenta ya existe")

    elif opcion == "2":
        print("su saldo es de:", saldo)

    elif opcion == "3":
        if cuenta_creada == False:
            print("crea una cuenta primero")
        else:
            monto = float(input("ingras la cantidad a depositar"))
            saldo += monto
            print("deposito exitoso")
    
    elif opcion == "4":
        if cuenta_creada == False:
            print("crea una cuenta primero")
        else:
            monto = float(input("ingrese la cantidad a retirar"))
        if monto <= saldo:
         saldo -= monto
         print("retiro exitoso")
        else:
            print("no tienes suficiente dinero")
    
    elif opcion == "5":
        print("gracias por usar tu mini banco de confianza")
        break



