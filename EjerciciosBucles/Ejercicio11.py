'''Ejercicio 11: Múltiplos
Escribe un programa que busque el primer número múltiplo de 7 que también sea mayor
que 80 y menor que 200. El programa debe saltar los números que no son múltiplos de 7 y
detenerse al encontrar el primero'''

Multiplo = False
primerMultiplo = 0

for i in range(80,200):
    if Multiplo == False:
        if i % 7 == 0:
            primerMultiplo = i
            Multiplo = True
print("El primer multiplo de 7 es:", primerMultiplo)

