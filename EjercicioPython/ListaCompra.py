"""
EJERCICIO: LISTA DE LA COMPRA   (RA1 y RA2)

Haz un programa en Python que gestione una lista de la compra:

1. Pregunta al usuario cuantos productos quiere comprar. Tiene que ser un
   numero entero mayor que 0. Si escribe otra cosa (por ejemplo "hola")
   hay que capturar el ValueError, mostrar un error y volver a preguntar.

2. Repite esa cantidad de veces:
   - Pide el nombre del producto y guardalo en la lista "productos".
   - Pide el precio y guardalo en la lista "precios". Si el precio no es
     un numero, captura el ValueError y vuelve a pedirlo.

3. Recorre la lista de productos con "for producto in productos" y
   muestralos por pantalla.

4. Recorre la lista de precios con "for precio in precios" para calcular
   el total de la compra.

5. Muestra el total y el producto mas caro.
"""

# ----------------------------------------------------------------------
# SOLUCION
# ----------------------------------------------------------------------

productos = []
precios = []

# pedir cuantos productos (hasta que sea un numero valido)
cantidad = 0
while cantidad <= 0:
    try:
        cantidad = int(input("Cuantos productos quieres comprar? "))
        if cantidad <= 0:
            print("Tiene que ser mayor que 0")
    except ValueError:
        print("Error, tienes que escribir un numero entero")

# pedir nombre y precio de cada producto
for i in range(cantidad):
    nombre = input("Nombre del producto: ")
    productos.append(nombre)

    valido = False
    while valido == False:
        try:
            precio = float(input("Precio de " + nombre + ": "))
            precios.append(precio)
            valido = True
        except ValueError:
            print("Error, el precio tiene que ser un numero")

# mostrar los productos
print("Lista de la compra:")
for producto in productos:
    print("-", producto)

# calcular el total
total = 0
for precio in precios:
    total = total + precio

# producto mas caro
mas_caro = productos[precios.index(max(precios))]

print("Total de la compra:", round(total, 2), "euros")
print("Producto mas caro:", mas_caro, "-", max(precios), "euros")