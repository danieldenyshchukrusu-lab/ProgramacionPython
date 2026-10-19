'''Ejercicio 10: Calcula inversión
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.
'''

cantidadInvertir = float(input("Introduce una cantidad a invertir"))
InteresAnual = float(input("Introduce el interes anual"))
numA = int(input("Introduce el numero de años"))
total = cantidadInvertir
interes = 0

for i in range(numA):
    interes = 0
    interes = total * InteresAnual
    total += interes
    print("El interes generado es de",interes,"y el total es de",total)
