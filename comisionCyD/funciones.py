"""def sumar(a,b):
    return a + b"""

#def restar(a,b):
#    return a - b


"""num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

resultado = sumar(num1,num2)
print(f"El resultado de la suma es: {resultado}")


num3 = int(input("Ingrese el primer numero: "))
num4 = int(input("Ingrese el segundo numero: "))

resultado2 = sumar(num3,num4)
print(f"El resultado de la suma es: {resultado2}")"""

"""num5 = int(input("Ingrese el primer numero: "))
num6 = int(input("Ingrese el segundo numero: "))

resultado3 = restar(num5,num6)
print(f"El resultado de la suma es: {resultado3}")"""

"""def describir_persona(nombre, edad):
    return f"Nombre: {nombre}\nEdad: {edad}"

datos= describir_persona(edad=30,nombre="José")

print(datos)"""

"""def calculate_total(*args):
    total = sum(args)
    return total

result = calculate_total(2, 4, 6, 8, 10, 25.5, 30, 100)
print(result) """ 


#Procedimientos

"""def imprimir_mensaje(nombre):
    print(f"Sos {nombre}")

imprimir_mensaje("Jorge")"""

"""def imprimir_numeros():
    for i in range(1, 11):
        print(i)

# Invocar al procedimiento
imprimir_numeros()
imprimir_numeros()
imprimir_numeros()"""

"""#variables locales y globales
def mi_funcion():
    x = 10  # Variable local
    print(x)

mi_funcion()

print(x)
 
# NameError: name 'x' is not defined"""

"""x = 10  # Variable global

def mi_funcion():
    print(x)

mi_funcion()  # Output: 10
print(x)  # Output: 10"""


#recursividad

"""def contar(numero):
    if numero == 0:  
        # Caso base: número es cero
        return
    else:  
        # Caso rec: contar uno por uno
        print(numero)
        contar(numero - 1)
contar(5)"""

"""def contar_hasta_cero(n):
    if n <= 0:  
        # Caso base
        print("¡Boom!")
    else:  
        # Caso recursivo
        print(n)
        contar_hasta_cero(n - 1)  

contar_hasta_cero(5)"""

"""n = 10

while n > 0:
    print(n)
    n = n - 1
print("Boom!")    

"""
        


    
