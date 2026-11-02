import random

'''Ejercicio 6: Adivina el número
El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Después
de cada intento, el programa indica si el número es mayor o menor. Usa try-except para
validar que la entrada sea numérica. El juego termina cuando el usuario acierta.
'''

numRandom = random.randint(1, 100)
try:
    print("Dado el numero random, adivine")
    num = -1
    while num != numRandom:
        num = int(input("Ingrese un numero: "))
        if (num > numRandom):
            print("El numero ",num," es mayor que el numero ingresado")
        if (num < numRandom):
            print("El numero ",num," es menor que el numero ingresado")
        if (num == numRandom):
            print("Has adivinado el numero")
except ValueError:
    print("ERROR: Entrada no numerica")