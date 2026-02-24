while True:
    print("\n---BIENVENIDO AL GESTOR DE GATOS---")
    print("1. agregar gastos")
    print("2. ver gastos ")
    print("3. ver total")
    print("4. salir")

    opcion = input("elige una de las siguentes opciones:")

    if opcion == "1":
        nombre = input("nombre del gasto")
        cantidad = float(input("cantidad"))
        with open("gastos.txt", "a") as archivo:
            archivo.write(nombre + "-" + str(cantidad) + "\n")
            print("gastos gaurdados")
    
    elif opcion == "2":
        with open("gastos.txt","r") as archivo:
           contenido = archivo.read()
           print("\n tus gastos:")
           print(contenido)
    elif opcion == "3":
        total = 0
        with open("gastos.txt","r") as archivo:
            for linea in archivo:
                partes = linea.strip().split("-")
                cantidad = float(partes[1])
                total += cantidad
                print("total de gastos:", total)
                break
        