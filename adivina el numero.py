import random
numero_secreto= random.randint(1,100)

while True:
    intento = int(input("adivina el numero:"))

    if intento > numero_secreto:
        print("muy alto")
    elif intento < numero_secreto:
        print("muy bajo")
    else:
        print("ganaste")
        break