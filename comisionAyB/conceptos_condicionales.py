"""#Condicional simple
print("===Confirmación de mayoria de edad===")
print("Buenas. Informenos su edad... ")
edad = int(input("Edad: "))

if edad >= 18:
    print("Sos mayor")
    
#Condicional compuesta

edad = int(input("Edad: "))

if edad >= 18:
    print("Sos mayor")
else:
    print("Sos menor")
    
print("Adios")   

#Condicional Múltiple
edad = int(input("Ingrese su edad: "))


if edad >= 30 and edad <= 110:
    print("Sos mayor edad, pero además tenes acceso a un descuento especial.")
elif edad >= 18 and edad <= 29:
    print("sos mayor de edad")
elif edad >= 1 and edad <= 17:
    print("Sos menor de edad.")
else:
    print("Edad incorrecta. Debe ser del 1 al 110.")
    
edad = 17

if edad < 18 or edad >= 65:
    print("Tenes derecho a un descuento")
else:
    print("No cumplis con ninguna condición")    
    
edad = 17

if (edad >= 18 and edad < 65) or (edad >= 65 and edad < 70):
#          False               or         False
    print("Eres elegible para votar.")    
else:
    print("No podes votar.")"""
    
    
"""1. Clasificación de nota
Situación: Ingresar una nota del 0 al 10 y mostrar si
el estudiante está:
● Desaprobado (0 a 5)
● Aprobado (6 a 8)
● Sobresaliente (9 o 10)   """ 

"""nota = int(input("Ingrese la nota: "))

if nota >= 0 and nota <= 5:
    print("Desaprobado")
elif nota >= 6 and nota <= 8:
    print("Aprobado")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("Nota inválida")"""
    
"""2. Par o impar
Situación: Pedir un número al usuario y decir si es
par o impar. """   


"""numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El Número {numero} es impar.")"""


"""5. Menú de opciones (condicional múltiple)
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
● Si elige otro número → mostrar "Opción inválida"""

"""print("=====Menú bancario=====")
print("1. Ver saldo")
print("2. Realizar transferencia")
print("3. Salir")

while True:
    opcion = input("Ingrese una opción del 1 al 3: ")

    if opcion == "1":
        print("Su saldo es $15.000")
    elif opcion == "2":
        print("Transferencia realizada con éxito")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")"""


    
    
    