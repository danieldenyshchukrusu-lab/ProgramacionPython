'''Ejercicio 3: Cuenta atrás
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
la cuenta atrás desde ese número hasta cero separados por comas.
'''

num = int(input("Introduce un numero entero positivo: "))
if num>=0:
    for i in range(num, 0, -1):
        print(i, end=",")
    print(0)
else:
    print("no")

