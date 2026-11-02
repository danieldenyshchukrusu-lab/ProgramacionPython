'''Ejercicio 7: Entradas de cine
Un cine cobra las entradas a distinto precio en función de la edad del espectador. Los
menores de 3 años entran gratis, los niños de entre 3 y 12 años pagan 8 € y la entradas
para mayores de 12 años cuesta 12 €.
● Calcula y muestra el precio de la entrada para 6 usuarios.
● Calcula y muestra el precio de la entrada hasta que el usuario introduzca un
valor negativo'''

numeroEntradas = int(input("Ingrese numero de entradas que va a comprar: "))
suma = 0
for i in range(numeroEntradas):
    edad = int(input("Introduce la edad de la persona"))
    if (edad>=0 and edad<3):
        suma += 0
    elif (edad>=3 and edad<=12):
        suma += 8
    else:
        suma += 12
print("El precio para ustedes es de:", suma)
