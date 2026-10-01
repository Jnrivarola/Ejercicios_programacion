"""Ciclo while

Escribe un programa que imprima los números del 1 al 10 utilizando un 
ciclo while."""

"""numero = 1

while numero < 11:
    print(numero)
    numero = numero + 1"""
    
"""Ciclo for
Crea un programa que recorra una lista de frutas y muestre cada fruta en 
la consola. Usa un ciclo for. """   

"""nombre = "Python"
frutas = ["Manzana","Banana","Ciruela","Sandía"]

for fruta in frutas:
    print(fruta)"""
    
"""Ciclo for
Crea un programa que solicite al usuario ingresar su nombre. 
Recorrer cada letra del nombre e imprimirlas de forma vertical.    """
# .lower() - .upper() - .capitalize()
"""nombre = input("Ingresa tu nombre: ")

for letra in nombre:
    print(letra)
print(f"Tu nombre tiene {len(nombre)} caracteres.")"""   

"""Uso de break
Escribe un programa que pida números al usuario hasta que se ingrese un número 
negativo.
Utiliza break para salir del bucle."""


"""while True:
    numero = int(input("Ingresa un número. (negativo para finalizar)"))
    if numero < 0:
        break"""
        
        
"""Ciclo do while (simulado con while)
Simula un ciclo do while en Python para pedir al usuario que ingrese 
una contraseña y verifica
si es correcta. Debe continuar pidiendo hasta que se ingrese 
la contraseña correcta. """       
#con do-while
"""while True:
    clave = input("Ingrese su clave: ")
    if clave == "clave123":
        print("Acceso correcto.")
        break
    else:
        print("Contraseña incorrecta. Intenta nuevamente.")"""
        
#con while

"""clave = input("Ingrese su clave: ")

while clave != "clave123":
    print("Contraseña incorrecta. Intenta nuevamente.")   
    clave = input("Ingrese su clave: ")
    
print("Acceso correcto") """        

