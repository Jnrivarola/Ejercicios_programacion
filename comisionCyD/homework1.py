"""Ejercicio N°1

Verificación de edad para ver una película

Supongamos que estás desarrollando un programa para un cine y deseas asegurarte de que los 
espectadores sean lo suficientemente mayores para ver una película clasificada como PG-13. 

Debes solicitar la edad del espectador y permitir el acceso solo si tienen al menos 13 años."""


print("===Bienvenido al Cine===")
print("=======Clasificación PG-13=========")

edad = int(input("Qué edad tenés?: "))

if edad >= 13:
    print("Podes pasar a ver la peli.")
else:
    print("No podes pasar. Te recomiendo otra peli")

