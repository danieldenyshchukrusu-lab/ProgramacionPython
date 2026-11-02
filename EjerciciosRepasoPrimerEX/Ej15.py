'''Ejercicio 5. Números repetidos
Dispones de dos listas de números enteros.
Utiliza dos bucles for anidados para encontrar los números que aparecen en ambas listas y
mostrarlos por pantalla.
Cada número común deberá mostrarse una sola vez.'''

numeros1 = 1,2,3,4,5,6,6
numeros2 = 2,3,3,8,5,6,6
numeros = []

for numero in numeros1:
    for numero2 in numeros2:
        if numero == numero2 and numero2 not in numeros:
            numeros.append(numero2)
print(numeros)

