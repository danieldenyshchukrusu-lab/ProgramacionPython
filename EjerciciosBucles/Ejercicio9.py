'''Ejercicio 9: Análisis de notas de alumnos
Crea un programa que dada una lista de las notas de un grupo de alumnos, calcule:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.'''

notas = [9,3,4,5,6]

cantidadTotalAprobados = 0
notaMedia = 0
notaAlta = 0
notaBaja = 10

for nota in notas:
    if nota >= 5:
        cantidadTotalAprobados += 1
    notaMedia += nota
    if nota >= notaAlta:
        notaAlta = nota
    if nota <= notaBaja:
        notaBaja = nota
print("Los alumnos que aprobaron",cantidadTotalAprobados)
print("Nota media de todos los alumnos",notaMedia/5)
print("La nota mas alta",notaAlta,"y la mas baja",notaBaja)
