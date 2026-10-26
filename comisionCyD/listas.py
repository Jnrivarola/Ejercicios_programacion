"""lista = ["Pedro","Ana", 3 , 4.5, True, False]
#           0      1     2   3     4     5

print(lista)

print(lista[4],lista[3])"""


"""temperaturas = [23, 28, 21, 25, 30]

print(temperaturas)

temperaturas[2]= 22

print(temperaturas)

for elemento in temperaturas:
    print(elemento)"""
    
"""mi_vector = [1,2,3,4,5,6]
print(mi_vector)

for i in range(len(mi_vector)):
    mi_vector[i] += 1   
    
print(mi_vector) """    

"""notas = [5, 5, 7,3]
suma = 0

for i in notas:
    suma += i    
promedio = suma / len(notas)

redondeo_promedio = round(promedio)

print("Promedio:", redondeo_promedio)

if redondeo_promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")"""
    
"""matriz = [[1, 2, 3], 
          [4, 5, 6]] 

print(matriz[0][2])   
"""

"""
#Intentar sacar el promedio de cada fila
notas = [[6, 7], 
         [8, 9], 
         [10, 6]]

for fila in notas:
    for valor in fila:
        print(valor)"""
        
"""cubo = [[[1,2],[3,4]],[[5,6],[7,8]]] 
#            0              1
#          0     1       0     1
#         0 1   0 1     0 1   0 1    

print(cubo[0][1][1])  """


"""torneo = [ [[1,2], [3,4]], [[5,6], [7,8]] ]
#                 0              1
#             0      1        0      1
#            0 1    0 1      0 1    0 1
print(torneo[0][1][0])"""

"""nombres_usuario = ["user1","user2","user3"]

for nombre in nombres_usuario:
    print(nombre)"""
    
"""numeros = [4, 8, 12, 16, 20]
print(numeros[6])  # ¿Qué valor imprime?  """  

#Listas
"""nombres_usuario = ["user1","user2","user3"]
nombres_usuario.append("user4")
print(nombres_usuario)
nombres_usuario.append("user6")
nombres_usuario.append("user7")
print(nombres_usuario)
nombres_usuario.pop(4)
print(nombres_usuario)
print(nombres_usuario.index("user3"))"""

"""tareas = ["leer", "escribir", "revisar"]
tareas[1] = "resumir"
print(tareas)
tareas.pop(0)
print(tareas)"""



#Tuplas
"""coordenadas = (10, 35)
transformacion_a_lista = list(coordenadas)
print(transformacion_a_lista)"""


#Set(conjuntos)
"""nombres = {"Ana","Juan","Hector","Ana"}
print(nombres)
nombres.add("Teresa")
print(nombres)
nombres.clear()
print(nombres)"""

#Dict(Diccionarios)

alumnos = [{"Nombre":"Gisela",
            "Apellido":"Flores",
            "Edad": 35},
{"Nombre":"Ana",
            "Apellido":"Gutierrez",
            "Edad": 20}]


