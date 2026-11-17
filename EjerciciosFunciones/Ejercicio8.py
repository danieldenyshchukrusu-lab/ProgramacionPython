'''Ejercicio 8: Generar tabla de multiplicar
Crea una función llamada `tabla_multiplicar` que reciba:
- numero (int)
- hasta (int), como argumento por palabra clave, con valor por defecto 10
La función debe devolver una lista con el resultado de la tabla de multiplicar del número
hasta el valor indicado.'''

def tabla_multiplicar(numero:int, hasta=10):
    resultados = []
    for i in range(1, hasta+1):
        resultados.append(numero*i)
    return resultados

print(tabla_multiplicar(2))
print(tabla_multiplicar(3))
print(tabla_multiplicar(4))