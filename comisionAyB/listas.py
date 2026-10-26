"""colores = ["azul", "rojo", "verde", "negro","violeta","blanco"]
#posicion    0       1       2         3        4        5

print(colores[0])"""

"""temperaturas = [23, 28, 21, 25, 30]
#                0   1   2   3   4

print("Primer día:", temperaturas[0]) 
print("Último día:", temperaturas[4])"""

#lista_varia= ["Matias","Pedro",4, 5.7, True, False]
"""print(lista_varia[1])
lista_varia[2]= "María"
print(lista_varia)"""

"""for elemento in lista_varia:
    print(elemento)"""
    
    
"""mi_vector = [1 ,2 ,3 ,4, 5]    

for i in range(len(mi_vector)):
    mi_vector[i] += 1
    
print(mi_vector)   """ 

"""notas = [5, 3, 9, 4, 7, 8]
suma = 0
for i in notas:
    suma += i
    
promedio = suma / len(notas)
promedio_redondeado = round(promedio)
print("Promedio:", promedio_redondeado)

if promedio_redondeado >= 6:
    print("Aprobado")
else:
    print("Desaprobado")"""

    
"""matriz = [[1, 2, 3] ,
          [4, 5, 6]]


print(matriz[1][2]) """ 


"""cubo = [[[1,2],[3,4]],[[5,6],[7,8]]] 
#             0             1
#          0     1       0     1
#         0 1   0 1     0 1   0 1

print(cubo[1][0][0])"""

"""torneo = [ [[1,2], [3,4]], [[5,6], [7,8]] ]
print(torneo[0][1][0])  # ¿Qué imprime?"""

"""usuarios = ["user1","user2","user3","user4"]

print(usuarios[6])"""

"""lista = ["Banana","Manzana","Pera"]
print(lista)
lista.append("Sandía")
print(lista)
lista.remove("Manzana")
print(lista)
print(lista.index("Pera"))"""

"""tareas = ["leer", "escribir", "revisar"]
tareas[1] = "resumir"
print(tareas)
tareas.pop(0)
print(tareas)"""

#Tuplas

"""usuarios = {"Jorge1","Romina2","Jorge1","Ana4"}
print(usuarios)
transformacion_usuarios = list(usuarios)
print(transformacion_usuarios)"""

usuario1 = [{"nombre":"Pedro",
            "apellido": "Fuentes",
            "edad": 35},
            {"nombre":"Ana",
            "apellido": "Flores",
            "edad": 25}]




