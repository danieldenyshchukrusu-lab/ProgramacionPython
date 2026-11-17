'''Ejercicio 1: Saludo personalizado
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.'''

def saludar(nombre: str, saludo="Hola"):
    return saludo + " " + nombre


print(saludar(nombre="Ana"))
print(saludar(nombre="Luis", saludo="Buenas"))