'''Ejercicio 11: Múltiplos
Escribe un programa que busque el primer número múltiplo de 7 que también sea mayor
que 80 y menor que 200. El programa debe saltar los números que no son múltiplos de 7 y
detenerse al encontrar el primero'''


'''contador = 1;
for i in range(81,200):
    if (i%7==0 and contador==1):
        print(i)
        contador = contador-1'''

noEncontrado = False
i = 81;

while i<200 and noEncontrado==False:
    if (i%7==0):
        noEncontrado = True
        print(i)
    i = i+1