# ---> Curso de Python de Midudev <---
# ! Módulo 3 - Clase 3 - La función range (03_range.py)
# * La función 'range()' genera una secuencia de números inmutable.
# * Se utiliza comúnmente con bucles 'for' para iterar un número específico de veces.
# ? Es esencial para crear secuencias numéricas de forma eficiente y controlar la ejecución de bucles.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

print("\nrange():")

# Ha generado una secuencia de números del 0 al 9.
for num in range(10):
    print(num)

# range(inicio, fin)
for num in range(5, 11):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 1000, 2):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

for num in range(0, 444, 2):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

for _ in range(5):
    print("Hacer algo 5 veces...")


###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for num in range(11):
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for num in range(1, 21, 2):
    print(num)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for num in range(5, 51, 5):
    print(num)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for num in range(10, 0, -1):
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for num in range(1, 101):
    suma += num
print(f"La suma de los números del 1 al 100 es: {suma}.")
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un número para ver su tabla de multiplicar: \n> "))
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")