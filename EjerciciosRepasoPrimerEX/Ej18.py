class NumeroNegativoError(Exception):
    pass

'''Ejercicio 8: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido'''

try:
    num = int(input("Introduce un numero entero positivo"))
    if num>=0:
        for numero in range(2, num + 1):
            es_primo = True
            divisor = 2

            while es_primo and divisor * divisor <= numero:
                if numero % divisor == 0:
                    es_primo = False
                divisor += 1

            if es_primo:
                print(numero)
    else:
        raise NumeroNegativoError("El numero no es positivo")
except NumeroNegativoError as e:
    print(e)
except ValueError:
    print("ERROR: Numero no valido")

