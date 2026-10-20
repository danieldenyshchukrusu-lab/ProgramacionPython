'''Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
entrada de datos no numéricos. '''

opcion = ""

while opcion != "SALIR":

    print("===MENU===")
    print("SUMA")
    print("RESTA")
    print("MULTIPLICACION")
    print("DIVISION")
    print("SALIR")

    opcion = input("Elige una opción")

    try:
        if opcion == "SUMA":

            numero1 = float(input("Primer numero para sumar"))
            numero2 = float(input("Segundo numero para sumar"))
            suma = numero1 + numero2
            print("El resultado es: " ,suma)

        elif opcion == "RESTA":

            numero1 = float(input("Primer numero para resta"))
            numero2 = float(input("Segundo numero para resta"))
            resta = numero1 + numero2
            print("El resultado es: " ,resta)

        elif opcion == "MULTIPLICACION":

            numero1 = float(input("Primer numero para multiplicar"))
            numero2 = float(input("Segundo numero para multiplicar"))
            multiplicacion = numero1 * numero2
            print("El resultado es: " ,multiplicacion)

        elif opcion == "DIVISION":

            numero1 = float(input("Primer numero para division"))
            numero2 = float(input("Segundo numero para division"))
            division = numero1 / numero2
            print("El resultado es: " ,division)

        elif opcion == "SALIR":

            print("¡Hasta luego!")

        else:

            print("Opcion no valida")

    except ValueError:

        print("valor introducido incorrecto")

    except ZeroDivisionError:

        print("No se puede dividir por 0")
