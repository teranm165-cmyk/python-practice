productos = {"pc":30,
             "monitor":40,
             "pantalla":30,}
carrito = []
total = 0

while True:
    print("---BIENVENIDO A TU PUNTO DE VENTA---")
    print("1. ver productos")
    print("2. agregar al carrito")
    print("3. ver carrito")
    print("4. eliminar del carrito")
    print("5. pagar")
    print("6. salir")

    opcion = input("por favor selecciona una opcion:")

    if opcion == "1":
          for producto, precio in productos.items():
               print(producto,"-",precio)
               
    elif opcion == "2":
         producto = input("ingrese el nombre del producto:")
         if producto in productos:
              precio = productos[producto]
              carrito.append([producto,precio])
         print("producto agregado al carrito exitosamente") 

    elif opcion == "3":
         carrito_vacio = 0
         if carrito == carrito_vacio:
              print("su carrito esta vacio")
         else:
              print("su carrito es:", carrito)

    elif opcion == "4":
         producto_eliminar = input("ingrese el nombre del producto a eliminar:")
         if productos in producto:
              producto_eliminar = productos[producto]
              carrito.pop(producto_eliminar)
              print("producto eliminado correctamente")

    elif opcion == "5":
         total = 0
         for item in carrito:
              total = total + item[1]
              print("el total a pagar es de:", total)

    elif opcion == "6":
         print("saliendo del programa")
         break


