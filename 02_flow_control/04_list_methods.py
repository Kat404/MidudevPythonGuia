# ---> Curso de Python de Midudev <---
# ! Módulo 2 - Clase 4 - Métodos de listas (04_list_methods.py)
# * Los métodos de listas son funciones incorporadas que permiten manipular y trabajar con listas de manera eficiente.
# * Facilitan tareas comunes como añadir, eliminar, ordenar y buscar elementos dentro de las listas.
# ? Dominar estos métodos es esencial para escribir código Python conciso y efectivo al manejar colecciones de datos.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# * Añadir elementos a una lista

lista1 = ['a', 'b', 'c', 'd']

lista1.append('e') # Añade un elemento al final de la lista
print(lista1)

lista1.insert(1, '@') # ? Inserta un elemento en una posición específica que le indicamos como primer argumento y el elemento a insertar como segundo argumento.
print(lista1)

lista1.extend(['f', 'g', 'h']) # Agrega elementos al final de la lista.
print(lista1)

# * Eliminar elementos de una lista
lista1.remove('@') # Elimina la primera ocurrencia del elemento indicado.
print(lista1)

ultimo = lista1.pop() # Elimina el último elemento de la lista y además lo devuelve.
print(ultimo)
print(lista1)

lista1.pop(1) # Elimina el segundo elemento de la lista (es el índice 1).
print(lista1)

# ? Otra forma de eliminar un elemento de la lista es usando la función 'del' y especificando el índice del elemento que queremos eliminar.
del lista1[-1]
print(lista1)

lista1.clear() # Elimina todos los elementos de la lista.
print(lista1)

# * Eliminar un rango de elementos
lista1 = ['a', 'b', 'c', 'd', 'e']
del lista1[3:] # Elimina los elementos desde el índice 1 hasta el 3 (excluyendo el 3).
print(lista1)

# * Más métodos útiles
print("\nOrdenar listas modificando la original:")

numbers = [3, 10, 2, 8, 99, 101]
numbers.sort() # Ordena la lista de menor a mayor modificando la original pero no devuelve una nueva lista.
print(numbers)

print("\nOrdenar listas creando una nueva lista:")
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers) # Ordena la lista de menor a mayor y crea una nueva lista.
print(sorted_numbers)
print(numbers)

print("\nOrdenar una lista de cadenas de texto (todo minúsculas):")
frutas = ['manzana', 'pera', 'limon', 'manzana', 'pera', 'limon']
sorted_frutas = sorted(frutas) # Ordena la lista de cadenas de texto alfabéticamente.
print(sorted_frutas)


print("\nOrdenar una lista de cadenas de texto (mezclas mayúsculas y minúsculas):")
frutas = ['manzana', 'Pera', 'Limon', 'manzana', 'pera', 'limon']
frutas.sort(key = str.lower) # Ordena la lista de cadenas de texto alfabéticamente ignorando mayúsculas.
print(frutas)

# ? Más cosas útiles
animals = ['panda', 'perro', 'koala', 'perro']
print(len(animals))            # Devuelve el número de elementos de la lista -> 4.
print(animals.count('perro'))  # Devuelve el número de veces que aparece el elemento 'perro' en la lista -> 2.
print('panda' in animals)      # Devuelve True si el elemento 'panda' está en la lista -> True.
print('hamster' in animals)    # Devuelve False si el elemento 'hamster' no está en la lista -> False.




print("\nEjercicios:")
###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

print("\nEjercicio 1:")
# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

numbers= [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(2, 10)
numbers[0] = 0
print(numbers)

print("\nEjercicio 2:")
# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
eliminado = lista_a.pop(3)
print(eliminado)
print(lista_a)
lista_b.clear()
print(lista_b)

print("\nEjercicio 3:")
# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers[2:5]
print(numbers)

print("\nEjercicio 4:")
# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

numbers = [5, 2, 8, 1, 9, 4, 2]
numbers.sort()
print(numbers)
print("Veces que aparece el número 2:", numbers.count(2))
print("El número 7 está en la lista:", 7 in numbers)

print("\nEjercicio 5:")
# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original

referencia[0] = 10
print(original)
print(copia_1)
print(copia_2)
print(referencia)

print("\nEjercicio 6:")
# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key = str.lower)
print(frutas)