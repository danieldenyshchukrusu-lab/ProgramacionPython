'''Ejercicio 9: Análisis de notas de alumnos
Crea un programa que dada una lista de las notas de un grupo de alumnos, calcule:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.
'''

notas = 9,2,3,6,5,7
alumnosAprobados = 0;
notaMedia = 0.0

for nota in notas:
    if (nota >=5):
        alumnosAprobados += 1
    notaMedia += nota

notaMaxima = max(notas)
notaMinima = min(notas)

print("La nota maxima de las notas es:",notaMaxima)
print("La nota minima de las notas es:",notaMinima)
print("La media de los alumnos es: ",notaMedia/len(notas))
print("Han aprobado ",alumnosAprobados)