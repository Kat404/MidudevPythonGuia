# ---> Curso de Python de Midudev <---
# ! Módulo 3 - Clase 2 - Bucles for (02_loop_for.py)
# * Los bucles 'for' permiten iterar sobre una secuencia de elementos (como listas, tuplas, diccionarios, strings).
# * Se utilizan cuando se sabe de antemano cuántas veces se necesita repetir el código o se quiere procesar cada elemento de una colección.
# ? Son esenciales para procesar colecciones de datos y realizar tareas repetitivas de forma controlada.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

print("\nBucles for:")

# Iterar una lista
frutas = ["manzana", "banana", "pera"]  # Lista de frutas
for fruta in frutas:  # Itera sobre cada fruta en la lista
    print(fruta)  # Imprime la fruta actual

# Iterar sobre cualquier cosa que sea iterable
cadena = "Python"  # Cadena de texto
for caracter in cadena:  # Itera sobre cada carácter en la cadena
    print(caracter)  # Imprime el carácter actual

# enumerate()
frutas = ["manzana", "banana", "pera"]  # Lista de frutas
for index, fruta in enumerate(frutas):  # Itera con índice y valor usando enumerate
    print(f"El índice es: {index} y la fruta es: {fruta}.")  # Imprime el índice y la fruta actual

# Bucles anidados
letras = ["A", "B", "C"]  # Lista de letras
numeros = [1, 2, 3]  # Lista de números

for letra in letras:  # Itera sobre cada letra
    for numero in numeros:  # Itera sobre cada número
        print(f"-> {letra}{numero}")  # Imprime la combinación de letra y número

# break
print("\nbreak:")  # Imprime un título para la sección de break
animales = ["gato", "perro", "mono", "elefante", "vaca", "loro"]  # Lista de animales
for idx, animal in enumerate(animales):  # Itera con índice y valor usando enumerate
    print(animal)  # Imprime el animal actual
    if animal == "mono":  # Verifica si el animal es "mono"
        print(f"El mono está escondido en el índice {idx}.")  # Imprime el índice del "mono"
        break  # Termina el bucle

# continue
print("\ncontinue:")  # Imprime un título para la sección de continue
animales = ["gato", "perro", "mono", "elefante", "vaca", "loro"]  # Lista de animales
for idx, animal in enumerate(animales):  # Itera con índice y valor usando enumerate
    if animal == "mono": continue  # Salta la iteración si el animal es "mono"
    print(animal)  # Imprime el animal actual

# Comprensión de listas (list comprehensions)
animales = ["gato", "perro", "mono", "elefante", "vaca", "loro"]  # Lista de animales
animales_mayus = [animal.upper() for animal in animales]  # Convierte cada animal a mayúsculas
print(animales_mayus)  # Imprime la lista de animales en mayúsculas

# Muestra los números pares de una línea
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]  # Filtra los números pares de la lista
print(pares)  # Imprime la lista de números pares


###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for num in range(2, 21, 2):
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print(f"La media de los números es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
maximo = max(numeros)
print(f"El número máximo en la lista es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: \n> ").lower()
contador = sum(1 for palabra in palabras if palabra[0].lower() == letra)
print(f"Hay {contador} palabras que empiezan con la letra '{letra}'.")



# ? No pude hacer los ejercicios por mi cuenta, me ayudó la IA de Cursor.
# ? Parece un buen instrumento pero al momento de tratar de hacer los ejercicios por mi cuenta simplemente los TABeo y la IA me hace spoiler de las soluciones.
# ? Incluso al hacer estos comentarios la IA sugiere texto que concuerda con lo que pienso.
# ? No me gusta, me da pena que la IA no pueda ser tan creativa como yo.