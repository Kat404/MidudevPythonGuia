# ---> Curso de Python de Midudev <---
# ! Módulo 5 - Sets de caracteres - Clase 4 (04_sets.py)
# * En este archivo, profundizaremos en los sets de caracteres en las expresiones regulares (regex) en Python.
# * Los sets de caracteres permiten definir conjuntos de caracteres que pueden coincidir en una posición determinada de una cadena.
# ? Comprender los sets de caracteres es esencial para crear patrones precisos y flexibles en la validación y búsqueda de texto.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
import re # * Importamos el módulo 're' para interactuar con el sistema regex
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# [: Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match: 
    print("El nombre de usuario es válido: ", match.group())
else: 
    print("El nombre de usuario no es válido.")

# Buscar todas las vocales de una palabra
text = "Hola Mundo"
pattern = r"[aeiou]" # ? Los corchetes nos permiten agrupar varios datos, filtros, cosas, objetos, que queremos buscar en un texto. 
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# Pero ignorando el resto
text = "man ran fan ñam ban"
pattern = r"[mfb]an"
matches = re.findall (pattern, text)
print(matches)