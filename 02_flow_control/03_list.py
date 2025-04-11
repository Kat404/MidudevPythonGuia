# ---> Curso de Python de Midudev <---
# ! Módulo 2 - Clase 3 - Listas (03_list.py)
# * Las listas son estructuras de datos que permiten almacenar múltiples elementos en una sola variable.
# * Se utilizan para guardar colecciones ordenadas de elementos que pueden ser de diferentes tipos.
# ? Son fundamentales para trabajar con conjuntos de datos y son una de las estructuras más versátiles de Python.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# * Creación de listas
print("\nCreación de listas:") # Imprime un título para la sección de creación de listas
lista1 = [1, 2, 3, 4, 5] # Lista de números enteros
lista2 = ["manzana", "naranja", "platano"] # Lista de strings/cadenas
lista3 = [1, "Hola", 3.1416, True] # Lista mixta

lista_vacia = [] # Lista vacía
lista_de_listas = [[1, 2], [3, 4], [5, 6]] # Lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(lista1) # Imprime el contenido de lista1
print(lista2) # Imprime el contenido de lista2
print(lista3) # Imprime el contenido de lista3
print(lista_vacia) # Imprime el contenido de lista_vacia
print(lista_de_listas) # Imprime el contenido de lista_de_listas
print(matrix) # Imprime el contenido de matrix

# * Acceso a elementos por índice
print("\nAcceso a elementos por índice:")
print(lista2[0]) #  Accede al primer elemento de la lista (manzana)
print(lista2[1]) #  Accede al segundo elemento de la lista (naranja)
print(lista2[-1]) #  Accede al último elemento de la lista (platano)
print(lista2[-2]) #  Accede al penúltimo elemento de la lista (naranja)

print(lista_de_listas[1][0]) #  Accede al primer elemento de la sublista (3)

# * Slicing (extraer sublistas/rebanado de listas)
lista1 = [1, 2, 3, 4, 5] # Reasigna lista1 con nuevos valores
print(lista1[1:4]) #  Extrae elementos desde el índice 1 hasta el 4 (excluyendo el 4) -> [2, 3, 4]
print(lista1[:3]) #  Extrae elementos desde el principio hasta el índice 3 (excluyendo el 3) -> [1, 2, 3]
print(lista1[3:]) #  Extrae elementos desde el índice 3 hasta el final -> [4, 5]
print(lista1[::2]) #  Extrae elementos desde el principio hasta el final, saltando de 2 en 2 -> [1, 3, 5]
print(lista1[::-1]) #  Extrae elementos desde el final hasta el principio, saltando de 1 en 1 -> [5, 4, 3, 2, 1]
print(lista1[:]) #  Extrae todos los elementos de la lista -> [1, 2, 3, 4, 5]

# * print(lista1[desde:hasta:paso])
# ? desde: inicio de la extracción
# ? hasta: fin de la extracción
# ? paso: cantidad de elementos a saltar
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Reasigna lista1 con más valores
print(lista1[::2]) #  Para devolver índices pares
print(lista1[::-1]) #  Para devolver la lista al revés

# * Modificar una lista
lista1[0] = 20 # Modifica el primer elemento de lista1 a 20
print(lista1) # Imprime el contenido modificado de lista1

# * Añadir elementos a una lista
lista1 = [1, 2, 3] # Reasigna lista1 con nuevos valores

# ? Forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6] # Concatena lista1 con otra lista y reasigna el resultado a lista1
print(lista1) # Imprime el contenido modificado de lista1

# ? Forma corta y más eficiente
lista1 += [7, 8, 9] # Añade elementos a lista1 usando el operador de asignación aumentada
print(lista1) # Imprime el contenido modificado de lista1

# * Recuperar longitud de una lista
print("Longitud de la lista:", len(lista1)) # Imprime la longitud (número de elementos) de lista1


###
# EJERCICIOS
###

print("\nEjercicio 1:")
# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"] # Define la lista mensaje original
mensaje_secreto = mensaje[7::] # Extrae los elementos desde el índice 7 hasta el final
print(mensaje_secreto) # Imprime la lista resultante 'mensaje_secreto'

print("\nEjercicio 2:")
# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50] # Define la lista de números original
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambia el primer y último elemento
print(numeros) # Imprime la lista con los elementos intercambiados

print("\nEjercicio 3:")
# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"] # Define la lista para el pan de arriba
ingredientes = ["jamón", "queso", "tomate"] # Define la lista de ingredientes
pan_abajo = ["pan abajo"] # Define la lista para el pan de abajo

sandwich = pan + ingredientes + pan_abajo # Concatena las tres listas para formar el sándwich
print(sandwich) # Imprime la lista resultante 'sandwich'

print("\nEjercicio 4:")
# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3] # Define la lista original
lista_duplicada = lista + lista # ? O lista * 2 es otra forma de duplicar la lista. # Crea una nueva lista concatenando la original consigo misma
print(lista_duplicada) # Imprime la lista duplicada

print("\nEjercicio 5:")
# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50] # Define la lista original
centro = len(lista) // 2 # Calcula el índice del elemento central usando división entera
print(lista[centro]) # Imprime el elemento en el índice central
# print(lista[2:3:2])

print("\nEjercicio 6:")
# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6] # Define la lista original
mitad = len(lista) // 2 # Calcula el índice de la mitad de la lista
lista_invertida = lista[:mitad][::-1] + lista[mitad:] # Invierte la primera mitad y la concatena con la segunda mitad
print(lista_invertida) # Imprime la lista con la primera mitad invertida
