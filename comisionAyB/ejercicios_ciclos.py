"""Ciclo while

Escribe un programa que imprima los números del 1 al 10 utilizando 
un ciclo while."""

"""contador = 1

while contador < 11:
    print(contador)
    contador = contador + 1"""
    
"""Ciclo for

Crea un programa que recorra una lista de frutas y muestre cada 
fruta en la consola. Usa un ciclo for."""


"""frutas = ["Manzana","Banana","Pera","Sandía"]

for elemento in frutas:
    print(elemento)"""
    
"""Ciclo for

Crea un programa que solicite al usuario ingresar su nombre. 
Recorrer cada letra del nombre e imprimirlas de forma vertical.  """  

"""nombre = input("Ingrese su nombre: ")

for letra in nombre:
    print(letra)

print(f"La cantidad de caracteres es: {len(nombre)}")"""


"""Uso de break

Escribe un programa que pida números al usuario hasta que se ingrese 
un número negativo.
Utiliza break para salir del bucle."""

"""while True:
    numero = float(input("Ingrese un número(negativo para finalizar): "))
    if numero < 0:
        break"""
        
"""Ciclo do while (simulado con while)
Simula un ciclo do while en Python para pedir al usuario que ingrese una 
contraseña y verifica si es correcta. 
Debe continuar pidiendo hasta que se ingrese la contraseña 
correcta. """       

"""while True:
    clave = input("Ingrese la clave: ")
    if clave != "clave123":
        print("Contraseña incorrecta. Intente denuevo.")
    else:
        print("Acceso correcto")
        break"""
        
"""while True:
    clave = input("Ingresa tu clave: ")  
    if clave != "clave123":
            print("Contraseña incorrecta. Intente denuevo.")
    if clave == "clave123":
        break

print("Acceso correcto!")"""        

"""clave = input("Ingrese la clave: ")

while clave != "clave123":
    print("Contraseña incorrecta. Intente nuevamente.")   
    clave = input("Ingrese la clave: ")
    
print("Acceso correcto")    """ 
        