'''Ejercicio 6: Adivina el número
El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Después
de cada intento, el programa indica si el número es mayor o menor. Usa try-except para
validar que la entrada sea numérica. El juego termina cuando el usuario acierta.'''
import random

numero = random.randint(1, 100)
adivinado = 0

print("Adivina el numero")

while adivinado != numero:
    try:
        adivinado = int(input("Ingrese un numero: "))

        if adivinado < numero:
            print("El numero es mayor que", adivinado)
        elif adivinado > numero:
            print("El numero es menor que", adivinado)

    except ValueError:
        print("introduce un numero valido")
else:
    print("Has adivinado el numero")