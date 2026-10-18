'''Ejercicio 2: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
error usando try-except.
'''

try:
    numero = int(input("Introduce un numero para mostrar su tabla de multiplicar"))
    for i in range(1,11):
        print(numero*i)
except ValueError:
    print("Error, valor no numerico")
