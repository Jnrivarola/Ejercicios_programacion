"""def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

#Operacion 1
num1 = 18
num2 = 20
resultado = sumar(num1,num2)

print(resultado)

#operacion 2
num3 = 30
num4 = 28.5
resultado2= sumar(num3,num4)

print(resultado2)

#operacion 3
num5 = int(input("Ingrese el primer número: "))
num6 = int(input("Ingrese el segundo número: "))

resultado3 = restar(num5,num6)
print(f"El resultado de la resta es: {resultado3}")"""


"""def describir_persona(nombre, edad, altura):
    return f"nombre: {nombre}\nedad: {edad}\naltura: {altura}"

# Uso de la función
resultado = describir_persona(edad=30,altura=1.70,nombre="Pepe")
print(resultado)"""

"""def calculate_total(*args):
    total = sum(args)
    return total

result = calculate_total(2, 4, 6, 8,10, 7, 4, 2,4.70)
print(result)  
# Output: 20"""

"""def sumar(a,b):
    return a+b
    
    


resultado = sumar(10,20)    
print(resultado)
resultado2 = sumar(30,50)
print(resultado2)"""

"""x = 20

def mi_funcion():
    x = 10 
    print(x)

mi_funcion()
print(x)"""

#recursividad

"""def contar_hasta_cero(n):
    if n <= 0:  
        # Caso base
        print("¡Boom!")
    else:  
        # Caso recursivo
        print(n)
        contar_hasta_cero(n - 1)  

contar_hasta_cero(10)"""

"""n = 10

while n > 0:
    print(n)
    n = n - 1
    
print("Boom!")  """   

"""def contar(numero):
    if numero == 0:  
        # Caso base: número es cero
        return
    else:  
        # Caso rec: contar uno por uno
        print(numero)
        contar(numero - 1)
contar(5)"""