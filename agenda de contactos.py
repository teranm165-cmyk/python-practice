while True:
    print("\n---BIENVENIDO A TU AGENDA DE CONTACTOS---")
    print("1. agregar contactos")
    print("2. ver contactos")
    print("3. buscar contactos")
    print("4. eliminar contactos")
    print("5. salir")

    opcion = input("selecciona una opcion")

    if opcion == "1":
        nombre = input("ingrese el nombre del contacto")
        numero = input("ingrese el numero del contacto")
        email = input("ingrese el email del contacto")

        linea_de_contacto = nombre + "," + numero +  "," + email + "\n" 

        with open("contactos.txt", "a") as archivo:
           archivo.write(linea_de_contacto)
           print("contacto guardado")

    elif opcion == "2":
        with open("contactos.txt", "r") as archivo:
            lista = archivo.readlines()
            for i, linea in enumerate(lista):
                print(i + 1, "-", linea.strip())

    elif opcion == "3":
        with open("contactos.txt", "r") as archivo:
            lista = archivo.readlines()
            nombre_buscar = input("ingrese el nombre del contacto a buscar")
            encontrado = False
            for i, linea in enumerate(lista):
                if not encontrado:
                    print("contacto no encontrado")
                if nombre_buscar in  linea.lower():
                    encontrado = True
                    print("contacto encontrado:", linea.strip())

    elif opcion == "4":
      with open("contactos.txt", "r" ) as archivo:
            lista = archivo.readlines()
            nombre_a_eliminar = input("ingrese del contacto a eliminar").lower()
            nueva_lista = []
            encontrado = False
            for linea in lista:
             if nombre_a_eliminar in linea.lower():
                encontrdo = True
             else:
                nueva_lista.append(linea)
      with open("contactos.txt", "w") as archivo:
                 archivo.writelines(nueva_lista)
                 print("contacto eliminado correctamente")
    
    elif opcion == "5":
        print("saliendo de la app")
        break



                    



