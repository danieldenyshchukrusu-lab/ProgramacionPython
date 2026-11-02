'''Ejercicio 10: Calcula inversión
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.
'''

cantidadInvertir = float(input("Introduzca la cantidad que quiere invertir"))
interesAnual = float(input("Introduzca el interes anual"))
numeroAños = int(input("Introduzca los años"))
total = 0;

for i in range(1,numeroAños):
    if (i==1):
        total = cantidadInvertir * interesAnual
        print(total)
    total = total * interesAnual
    print(total)

