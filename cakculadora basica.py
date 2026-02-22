#calculadora basica

while True:

  num1 = float(input ("ingrese el primer numero"))
  num2 = float (input("ingrese el segundo numero"))

  print("operaciomes")
  print("1:suma")
  print("2:resta")
  print("3:multiplicacion")
  print("4:division")

  operacion = input("elige una operacion")

  if (operacion == "1"):
    resultado = num1 + num2
    print(resultado)
  elif (operacion == "2"):
    resultado = num1 - num2
    print(resultado)
  elif (operacion == "3"):
    resultado = num1  * num2
    print(resultado)
  elif (operacion == "4"):
    resultado = num1 / num2
    if num2 == 0:
        print("error:no se puede dividir entre cero")
  else:
     resultado = num1 / num2
     print(resultado) 

  intentar_de_nuevo = input("quieres salir la calculadora (si/no):").lower()

  if intentar_de_nuevo == "si":
   print("gracias por usarme")
   break