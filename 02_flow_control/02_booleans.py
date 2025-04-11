# ---> Curso de Python de Midudev <---
# ! Módulo 2 - Clase 2 - Valores Booleanos (02_booleans.py)
# * Los valores booleanos (bool) son un tipo de dato que solo puede tener dos valores: True o False.
# * Se utilizan para representar condiciones y son fundamentales en las estructuras de control de flujo.
# ? Son la base para la lógica de programación y la toma de decisiones en Python.

import os
os.system("cls")

"""
Este código importa el módulo 'os' y utiliza la función system() para limpiar
la pantalla de la consola antes de mostrar los resultados del programa.
En sistemas Windows, el comando 'cls' limpia la pantalla.
En sistemas Unix/Linux, se usaría 'clear' en su lugar.
"""

print("\nValores booleanos básicos:")
print(True)
print(False)

# ? Operadores de comparación: devuelven un valor booleano
print("\n Operadores de comparación:")
print("5 > 3:", 5 > 3) # True
print("5 < 3:", 5 < 3) # False
print("5 == 5:", 5 == 5) # True (igualdad)
print("5 != 3:", 5 != 3) # True (diferencia/desigualdad)
print("5 >= 5:", 5 >= 5) # True (mayor o igual que)
print("5 <= 3:", 5 <= 3) # False (menor o igual que)

print("\nComparación de cadenas:")
print("manzana < pera:", "manzana" < "pera") # True
print("'Hola' == 'hola':", "Hola" == "hola") # False

# ? Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False) # False
print("True or False:", True or False)   # True
print("False or False:", False or False) # False
print("not True:", not True)             # False
print("not False:", not False)           # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")

print("\nand:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\nor:")
print("A     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\nnot:")
print("A        not A")
print("True    ", not True)
print("False   ", not False)