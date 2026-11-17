'''Ejercicio 3: Crear usuario con lista
Crea una función llamada `crear_usuario` que reciba los siguientes argumentos por palabra
clave:
- nombre (str)
- email (str)
- activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos con los datos del usuario en
el orden: [nombre, email, activo].'''

def crear_usuario(nombre:str, email:str, activo = True):
    if activo:
        return [nombre, email, activo]
    return []

print(crear_usuario('Daniel','daniel.denyshchuk@educa.madrid.org'))
print(crear_usuario('Bingo','bingo.denyshchuk@educa.madrid.org',False))

