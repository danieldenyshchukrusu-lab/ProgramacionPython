'''Ejercicio 3: Cuenta atrás
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
la cuenta atrás desde ese número hasta cero separados por comas.
'''

numero = int(input("Ingrese un numero: "))
if numero > 0:
    for i in range(numero, 0, -1):
        print(i, end=","); '''Normalmente print termina con un salto de línea, y por eso cada número saldría en una línea distinta. Con end="," le dices: “al terminar, en vez de saltar de línea, escribe una coma”. Así todo sale seguido:'''
    print(0); '''como esto esta fuera del bucle simplemente pondra 0 y ya'''
else:
    print("Error, el numero no es positivo")