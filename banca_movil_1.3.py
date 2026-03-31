class Bancamovil:
    def __init__(self,titular,saldo,historial):
        self.titular = titular
        self.saldo = saldo
        self.historial = historial
        

    def depositar(self):
      cantidad_a_depositar = int(input("cuanto dinero quiere depositar"))
      self.saldo += cantidad_a_depositar
      self.historial.append(f"deoposito: + {cantidad_a_depositar}")
      print(f"deposito exitoso su saldo es {self.saldo}")
   



    def transferir(self):
      cantidad_a_transferir = int(input("cuanto dinero quiere transferir"))
      if cantidad_a_transferir > self.saldo:
        print("saldo insuficiente")
      else:
          self.saldo -= cantidad_a_transferir
          self.historial.append(f"transferencia: - {cantidad_a_transferir}")
      print(f"tramsferencia exitosa su saldo ahora es de: {self.saldo}")
 
     
    

    def mostrar_historial(self):
      print(f"su historial es : {self.historial}")

titular = "miguel"
saldo = 2000
historial = []
     

usuario1 = Bancamovil(titular,saldo,historial)


while True:
   print("--BIENVENIDO A TU BANCA--")
   print("1. depositar")
   print("2. tranferir")
   print("3. historial")

   opcion = input("seleccione una opcion")
   
   if opcion == "1":
      usuario1.depositar()

   elif opcion == "2":
      usuario1.transferir()

   elif opcion == "3":
      usuario1.mostrar_historial()
      

   








