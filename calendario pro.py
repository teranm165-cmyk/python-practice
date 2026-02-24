import datetime

eventos = []

while True:
    print("\n---BIENVENIDO A TU CALENDARIO---")
    print("1. fecha de hoy")
    print("2. agrgar eventos de hoy")
    print("3. ver eventos")
    print("4. salir")

    opciom = input("elige una opcion")

    if opciom == "1":
        hoy = datetime.date.today()
        print("la fecha de hoy es:", hoy)
    elif opciom == "2":
        fecha_evento = input("ingresa la fecha del evento (AAAA-MM-DD):")
        descripcion = input("ingresa alguna descripcion")
        evento = {"fecha":fecha_evento,"descripcion":descripcion}
        eventos.append(evento)
        print("eventos agregado correctamente")
    elif opciom == "3":
        if len(eventos) == 0:
            print("no hay eventos registrados")
        else:
            print("tus eventos")
            for evento in eventos:
                print("_ {}: {}.".format(evento["fecha"],evento["descripcion"]))
    elif opciom == "4":
        print("saliendo del calendario")
        break

