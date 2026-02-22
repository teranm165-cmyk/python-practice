import random
longitud = int(input("cuantos caracteres quieres en tu contraseña"))
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "123456789"
simbolos = "!@#$%^&*()"

ingredientes = letras_minusculas + letras_mayusculas + numeros + simbolos

contraseña = ""
for i in range(longitud):
    contraseña += random.choice(ingredientes)


print("tu contraseña es:", contraseña)