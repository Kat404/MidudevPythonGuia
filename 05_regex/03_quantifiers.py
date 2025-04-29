# ---> Curso de Python de Midudev <---
# ! Módulo 5 - Cuantificadores - Clase 3 (03_quantifiers.py)
# * En este archivo, profundizaremos en los cuantificadores de las expresiones regulares (regex) en Python.
# * Los cuantificadores permiten definir la cantidad de veces que un carácter, grupo o patrón puede aparecer en una cadena.
# ? Comprender los cuantificadores es esencial para crear patrones flexibles y potentes en la validación y búsqueda de texto.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
import re # * Importamos el módulo 're' para interactuar con el sistema regex
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)


# *: Puede aparecer 0 o más veces.
text = "aaaba"
pattern = "a*"  # ? Coincide con 0 o más 'a'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)