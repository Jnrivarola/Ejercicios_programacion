"""Situación: Ingresar una nota del 0 al 10 y mostrar si
el estudiante está:
● Desaprobado (0 a 5)
● Aprobado (6 a 8)
● Sobresaliente (9 o 10)
"""

"""nota = int(input("Ingresa la nota(del 0 al 10): "))

if nota >= 0 and nota <= 5:
    print("Desaprobado")
elif nota >= 6 and nota <= 8:
    print("Aprobado")
elif nota == 9 or nota == 10:
    print("Sobresaliente")
else:
    print("Nota inválida")"""
    
"""Par o impar
Situación: Pedir un número al usuario y decir si es
par o impar.  """  

"""numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")"""
    

"""Menú de opciones (condicional múltiple)
Situación: El programa debe simular un menú bancario
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
● Si elige otro número → mostrar "Opción inválida"   """

"""print("====Menú bancario====")
print("1. Ver saldo") 
print("2. Realizar transferencia")
print("3. Salir")  

opcion = int(input("Elija una opción(1, 2 o 3): "))

while opcion != 3:
    if opcion == 1:
        print("Su saldo es $15.000")
    elif opcion == 2:
        print("Transferencia realizada con éxito")
    else:
        print("Opción inválida.")
    opcion = int(input("Elija una opción(1, 2 o 3): "))
        
print("Saliendo del sistema...")"""        