"""1. Clasificación de nota
Situación: Ingresar una nota del 0 al 10 y mostrar si
el estudiante está:
● Desaprobado (0 a 5)
● Aprobado (6 a 8)
● Sobresaliente (9 o 10)

nota = int(input("Ingrese la nota del 0 al 10: "))

if nota >= 0 and nota <= 5:
    print("Desaprobado")
elif nota >= 6 and nota <= 8:
    print("Aprobado")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("Nota inválida. debe elegir del 0 al 10.")"""
    
"""Par o impar
Situación: Pedir un número al usuario y decir si es
par o impar.   

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")"""
    
"""Mayor de tres números
Situación: Ingresar tres números y mostrar cuál es el
mayor de los tres.   

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor")
else:
    print(f"{num3} es el mayor")"""
    
"""Situación: Pedir la edad del usuario y mostrar:
● "Acceso denegado" si es menor de 18
● "Acceso permitido" si tiene 18 o más 

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado") """  
    
"""Situación: El programa debe simular un menú bancario
simple.
Mostrar el siguiente menú al usuario:
1. Ver saldo
2. Realizar transferencia
3. Salir
El usuario debe ingresar un número del 1 al 3 según la opción
que quiera. El programa mostrará un mensaje correspondiente:
● Si elige 1 → mostrar "Su saldo es $15.000"
● Si elige 2 → mostrar "Transferencia realizada con éxito"
● Si elige 3 → mostrar "Saliendo del sistema..."
● Si elige otro número → mostrar "Opción inválida"    

print("=====Menú bancario=====")
print("Opciones...")
print("1. Ver saldo")
print("2. Realizar transferencia")
print("3. Salir")

opcion = int(input("Elija una opción: "))

if opcion == 1:
    print("Su saldo es $15.000")
elif opcion == 2:
    print("Transferencia realizada con éxito")
elif opcion == 3:
    print("Saliendo del sistema...")
else:
    print("Opción inválida") """
