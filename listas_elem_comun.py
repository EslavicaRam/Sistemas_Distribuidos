# 
"""
Alumna: Ramírez Flores Eslavica Montserrat
Código en Python para crear una función para obtener 
los elementos comunes de una lista
"""
def element_comunes(lista_1, lista_2):
    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)

    return list(conjunto_1 & conjunto_2)


numeros_1 = [1, 2, 3, 4, 5, 6]
numeros_2 = [3, 4, 7, 9, 10]

resultado = element_comunes(numeros_1, numeros_2)

print(resultado) 