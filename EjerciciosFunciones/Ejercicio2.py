'''Ejercicio 2: Cálculo de precio con IVA
Crea una función llamada `calcular_precio` que reciba:
- precio_base (float)
- iva (float), como argumento por palabra clave, con valor por defecto 21
La función debe devolver el precio final con el IVA aplicado.'''

def calcular_precio(precio_base, iva=21):
    return precio_base * (1 + iva / 100)

print(calcular_precio(100))
print(calcular_precio(100, iva=10))