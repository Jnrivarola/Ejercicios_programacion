#SORT
"""lista = [54,20,10,50,12,12,36,1,5]
print(lista)

lista.sort()

print(lista)"""

#SORTED
"""lista = [54,20,10,50,12,12,36,1,5]
print(lista)
lista_ordenada = sorted(lista)
print(lista_ordenada)"""

#DESCENDENTE
"""lista = [54,20,10,50,12,12,36,1,5]
print(lista)

lista.sort(reverse=True)
print(lista)"""

"""lista_original = [54,20,10,50,12,12,36,1,5]
print(lista_original)
orden_descendente = sorted(lista_original,reverse=True)
print(orden_descendente)"""

"""nombres = ["Lucrecia","Ana","Alana","Noemi","Alex","Franco"]
nombres.sort()
print(nombres)
print(nombres.index("Alana"))"""

"""nombres_originales = ["Lucrecia","Ana","Alana","Noemi","Alex","Franco"]
nombres_ordenados = sorted(nombres_originales)
nombres_ordenados_descendente = sorted(nombres_originales,reverse=True)
print(nombres_ordenados_descendente)"""


#==============================================================================
#Busqueda lineal
"""def buscar_linealmente(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Ejemplo de uso
lista = [3, 5, 2, 4, 9]
resultado = buscar_linealmente(lista, 9)  
# Devuelve 3

print(resultado)"""

#Busqueda binaria
def binary_search(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = binary_search(lista, 4)  # Devuelve 3

print(resultado)

