pin_secreto = 1234
saldo = 2000
intentos = 0
sesion_activa = False
print("---BIENVENIDO A TU BANCA---")
while intentos < 3:
    ingreso = int(input("intoduzca su pin"))
    if ingreso == pin_secreto:
        sesion_activa = True
        break
    else:
        intentos += 1
        print(f"PIN icorrecto, Te quedan {3 - intentos} intentos.")
if sesion_activa:
    while True:
       print("\n1. consultar saldo")
       print("2. transferencia")
       print("3. depositar")
       print("4. salir")

       opcion = input("elige una opcion")

       if opcion == "1":
           print("su saldo es de:", saldo)
                
       elif opcion == "2":
         transferencia = int(input("cuanto dinero quiere tranferir:"))
         saldo -= transferencia
         print("transferecia exitosa")

       elif opcion == "3":
        depositar = int(input("cuanto dinero quiere depositar"))
        saldo += depositar
        print("deposito exitoso")

       elif opcion == "4":
         print("saliendo del programa")
         break

