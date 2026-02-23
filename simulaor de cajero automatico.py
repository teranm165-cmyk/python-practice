saldo = 1000

while True:
    print("\n---CAJERO AUTOMSTICO---")
    print("1.ver saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("4, salir")

    opcion = input("escoge una opcion: ")

    if opcion == "1":
        print('su saldo es de:', saldo)
    elif opcion == "2":
        deposito = float(input("cuanto dinero quiere depositar"))
        saldo += deposito
        print("dinero depositado correctamente")

    elif opcion == "3":
        retiro = float(input("cuanto dinero quiere retirar"))
        if retiro <= saldo:
           saldo -= retiro 
           print("retiro exitoso")
        else:
            print("no tienes suficiente dinero")
    

    elif opcion == "4":
        print("gracias por usar el cajero")
        break

    
        
