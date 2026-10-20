class EntradasMenosQueOIgual0 (Exception):
    pass
class EntradasMasQueEntradasRestantes (Exception):
    pass

entradas = 25
opcion = 0

print("===MENU===")
print("===1. COMPRAR ENTRADAS==")
print("===2. MOSTRAR ENTRADAS DISPONIBLES===")
print("===3. SALIR===")
while opcion != 3:
    try:
        opcion = int(input("Introduzca una opcion: "))
        if opcion == 1:
            numeroEntradas = int(input("Ingrese numero de entradas las cual quiera comprar: "))
            if numeroEntradas > entradas:
                raise EntradasMasQueEntradasRestantes("ERROR. Has solicitado mas entradas de las que quedan")
            elif numeroEntradas <= 0:
                raise EntradasMenosQueOIgual0("ERROR. Has solicitado 0 o menos entradas")
            else:
                entradas = entradas - numeroEntradas
        elif opcion == 2:
            print("el numero de entradas que quedan disponibes es de:",entradas)
        else:
            print("Opcion invalida")
    except ValueError:
        print("Error al ingresar")
    except EntradasMasQueEntradasRestantes as e:
        print(e); '''Si quiero que los errores se vean como mensaje en vez de error, lo que hacemos es lo siguiente.'''
    except EntradasMenosQueOIgual0 as e:
        print(e)
print("saliendo del programa")



