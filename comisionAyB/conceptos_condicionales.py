#Condicional simple
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
    print("No podes votar.")
    
    
    