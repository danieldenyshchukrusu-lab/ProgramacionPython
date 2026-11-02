'''Ejercicio 4. Menús del restaurante
Un restaurante ofrece varias comidas y varias bebidas.
Utiliza dos bucles for anidados para mostrar todas las combinaciones posibles de comida y
bebida.
Cada línea deberá mostrar una combinación diferente.
'''

comidas = "pizza","hamburguesa","spaggueti"
bebidas = "fanta","cocacola","agua"

for comida in comidas:
    for bebida in bebidas:
        print(comida,"con",bebida)