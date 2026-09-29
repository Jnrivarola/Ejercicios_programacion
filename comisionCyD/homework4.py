"""Ejercicio N°4

Validar dias de la semana

Crea un programa que pida al usuario ingresar un número del 1 al 7 
y muestre el día de la semana correspondiente. Si ingresa un número 
fuera de ese rango, mostrar el siguiente 
mensaje de error: Número de día incorrecto."""

numero_dia = input("Ingrese un día de la semana: ").upper()

if numero_dia == "domingo":
    print("Domingo")
elif numero_dia == "lunes":
    print("Lunes")
elif numero_dia == "martes":
    print("Martes")
elif numero_dia == "miércoles":
    print("Miércoles")
elif numero_dia == "jueves":
    print("Jueves")
elif numero_dia == "viernes":
    print("Viernes")
elif numero_dia == "sabado":
    print("Sábado")
else:
    print("Día inválido. Debe elegir del 1 al 7.")