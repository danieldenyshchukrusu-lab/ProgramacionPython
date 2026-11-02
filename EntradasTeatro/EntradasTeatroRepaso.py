class NoQuedanEntradas(Exception):
    pass

class MenorOIgualCero(Exception):
    pass

'''Ejercicio 1: Venta de entradas de teatro
Un teatro dispone inicialmente de 25 entradas disponibles. Desarrolla un programa en Python
que permita comprar entradas mediante un menú con las siguientes opciones:
1. Comprar entradas.
2. Mostrar entradas disponibles.
3. Salir.
Debes tener en cuenta que:
● Al seleccionar la opción Comprar entradas, el programa solicitará el número de
entradas que desea comprar el cliente.
● Si la venta es correcta, se actualizará el número de entradas disponibles.
● El programa deberá repetirse hasta que el usuario seleccione la opción Salir.
● Tanto si el usuario introduce un valor no numérico, como si solicita una cantidad de
entradas menor o igual que cero o si solicita más entradas de las que quedan
disponibles, se debe controlar usando excepciones específicas.
● Además, el programa deberá controlar opciones de menú no válidas. (no es necesario
utilizar excepciones)'''

entradasDisponibles = 25
opcion = 0

try:
    print("===MENU===")
    print("1. Comprar entradas.")
    print("2. Mostrar entradas disponibles.")
    print("3. Salir.")
    while (opcion != 3):
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            numeroComprar = int(input("Ingrese el numero de entradas que quiera comprar: "))
            if (numeroComprar <= 0):
                raise MenorOIgualCero("ERROR: numero cero o menor no valido")
            if (entradasDisponibles >= numeroComprar):
                entradasDisponibles = entradasDisponibles - numeroComprar
                print("Ha comprado",numeroComprar,"entradas")
            elif (entradasDisponibles <= numeroComprar):
                raise NoQuedanEntradas("ERROR: No hay suficientes entradas disponibles")
        elif opcion == 2:
            print("quedan: ",entradasDisponibles,"disponibles")
        elif opcion == 3:
            print("Saliendo del programa...")
        else:
            print("opcion no valida, elija otra opcion")
except ValueError:
    print("Valor no valido")
except NoQuedanEntradas as e:
    print(e)
except MenorOIgualCero as e:
    print(e)