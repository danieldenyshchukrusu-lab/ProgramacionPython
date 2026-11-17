'''Ejercicio 4: Formatear nombre completo
Crea una función llamada `formatear_nombre` que reciba:
- nombre (str)
- apellido (str)
- orden (str), con valor por defecto "nombre_apellido" (el otro valor que podría tomar sería
apellido_nombre)
La función debe devolver el nombre completo en el orden indicado.'''

def formatear_nombre(nombre:str, apellido:str, orden="nombre_apellido"):
    if orden == "nombre_apellido":
        return nombre + " " +apellido
    else:
        return apellido + " " + nombre

print(formatear_nombre("David","hernandez"))
print(formatear_nombre("David","fernandez","apellido_nombre"))