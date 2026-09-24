"""Ejercicio N°2

Calificación de un estudiante
Imagina que eres un profesor y deseas calcular las calificaciones 
finales de tus estudiantes en función de sus puntajes en un examen.  
La calificación final se asignará de la siguiente manera: 

Si el puntaje…
Es mayor o igual a 90, la calificación es "A".
Está entre 80 y 89, la calificación es "B".
Está entre 70 y 79, la calificación es "C".
Está entre 60 y 69, la calificación es "D".
Es menor que 60, la calificación es "F"."""

calificacion = 1

if calificacion >= 90:
    print('La calificación es "A"')
elif calificacion > 79:
    print('La calificación es "B"')
elif calificacion > 69:
    print('La calificación es "C"')
elif calificacion > 59:
    print('La calificación es "D"')
elif 0 < calificacion < 60:
    print("La calificación es 'F'")
else:
    print("Número inválido")
    
    
    
  
