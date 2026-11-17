'''Ejercicio 7: Filtrar números pares
Crea una función llamada `filtrar_pares` que reciba una lista de números enteros y devuelva
una nueva lista solo con los números pares.'''

def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


print(filtrar_pares([1, 2, 3, 4, 5, 6]))
print(filtrar_pares([7, 9, 11]))