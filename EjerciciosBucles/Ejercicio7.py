'''Ejercicio 7: Entradas de cine
Un cine cobra las entradas a distinto precio en función de la edad del espectador. Los
menores de 3 años entran gratis, los niños de entre 3 y 12 años pagan 8 € y la entradas
para mayores de 12 años cuesta 12 €.
● Calcula y muestra el precio de la entrada para 6 usuarios.
● Calcula y muestra el precio de la entrada hasta que el usuario introduzca un
valor negativo'''

'''Calcula y muestra el precio de la entrada para 6 usuarios.'''

cantidadPersonas = int(input("Introduce para cuantas personas quiere entrada"))
cantidadTotal = 0

for i in range(cantidadPersonas):

    edad = int(input("Introduzca la edad de la persona"))

    if edad < 3:
        cantidadTotal += 0
    elif edad >= 3 and edad <= 12:
        cantidadTotal += 8
    else:
        cantidadTotal += 12
print("La cantidad total que tiene que pagar por las",cantidadPersonas,"es de ",cantidadTotal)

'''Calcula y muestra el precio de la entrada hasta que el usuario introduzca un
valor negativo'''

seguir = True

while seguir == True:
    cantidadPersonas = int(input("Introduce para cuantas personas quiere entrada (negativo para salir): "))

    if cantidadPersonas < 0:
        seguir = False
    else:
        cantidadTotal = 0

        for i in range(cantidadPersonas):
            edad = int(input("Introduzca la edad de la persona: "))

            if edad < 3:
                cantidadTotal += 0
            elif edad <= 12:
                cantidadTotal += 8
            else:
                cantidadTotal += 12

        print("La cantidad total que tiene que pagar por las", cantidadPersonas, "personas es de", cantidadTotal)

print("Hasta luego")