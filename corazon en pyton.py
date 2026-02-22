import turtle

# Configuración inicial
t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("white")  # Fondo blanco
t.color("red", "pink")   # Borde rojo, relleno rosa

# Función para dibujar corazón
def dibujar_corazon():
    t.begin_fill()
    t.left(50)
    t.forward(100)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(100)
    t.end_fill()

# Dibujar corazón
dibujar_corazon()

# Escribir "TE AMO" dentro
t.up()
t.setpos(0, 20)  # Posición del texto
t.down()
t.color("darkred")
turtle.hideturtle()
turtle.write("TE AMO", align="center", font=("Arial", 24, "bold"))

# Mantener ventana abierta
turtle.done()