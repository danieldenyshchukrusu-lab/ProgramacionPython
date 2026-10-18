'''Ejercicio 5. Números repetidos
Dispones de dos listas de números enteros.
Utiliza dos bucles for anidados para encontrar los números que aparecen en ambas listas y
mostrarlos por pantalla.
Cada número común deberá mostrarse una sola vez.
'''

numeros1 = [1,2,3,4,5,6,6,6]
numeros2 = [1,2,3,4,5,7,6,6]

comunes = set(numeros1) & set(numeros2); '''convierte la lista en un conjunto, que no admite repetidos.'''

for numero in comunes:
    print(numero)
