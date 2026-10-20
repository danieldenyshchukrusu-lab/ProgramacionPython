'''Ejercicio 8: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido.

(MAL HECHO, TENGO QUE ENSEÑAR TODOS LOS NUMEROS PRIMOS, NO SOLO UNO XD)
'''

try:
    contador = 0

    numero = int(input("Introduce un numero entero positivo para obtener sus numeros primos: "))
    for n in range(numero, 2 , -1):
        if numero % n == 0:
            contador += 1

    if contador == 1:
        print("El numero", numero, "es primo")
    else:
        print("El numero", numero, "no es primo")
except ValueError:
    print("Valor invalido")