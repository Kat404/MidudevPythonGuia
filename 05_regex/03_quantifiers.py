# ---> Curso de Python de Midudev <---
# ! Módulo 5 - Cuantificadores - Clase 3 (03_quantifiers.py)
# * En este archivo, profundizaremos en los cuantificadores de las expresiones regulares (regex) en Python.
# * Los cuantificadores permiten definir la cantidad de veces que un carácter, grupo o patrón puede aparecer en una cadena.
# ? Comprender los cuantificadores es esencial para crear patrones flexibles y potentes en la validación y búsqueda de texto.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
import re # * Importamos el módulo 're' para interactuar con el sistema regex
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)


# * --> *: Puede aparecer 0 o más veces.
text = "aaaba"
pattern = "a*"  # ? Coincide con 0 o más 'a'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)

# Ejercicio 1:
# ¿Cuántas palabras tienen de 0 a más "a" y después una "b"?

# * --> +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"  # ? Coincide con 1 o más 'a'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)

# * --> ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"  # ? Coincide con 0 o 1 'a' seguido de 'b'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)

# Ejercicio 2:
# Haz opcional que aparezca un +52 en el siguiente texto
phone = "+52 5512345678"
pattern = r"(\+|00)?52 \d{9}"
found = re.findall(pattern, phone)
print(found)

# * --> {n}: Exactamente n veces
text = "aaaabbbccc"
pattern = "a{3}"  # ? Coincide con exactamente 3 'a'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)

# * --> {n, m}: De n a m veces
text = "z zz zzz zzzz"
pattern = "z{2,3}"  # ? Coincide con 2 o 3 'z'
matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)

# Ejercicio 3:
# Encuentra las palabras de más de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león circo murciélago"
pattern = r"\b\w{4,6}\b"
long_words = re.findall(pattern, words)
print(long_words)

print("\n")

# Ejercicio 4:
# Encuentra las palabras de más de 6 letras
words = "ala fantástico casa árbol león cinco murciélago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)