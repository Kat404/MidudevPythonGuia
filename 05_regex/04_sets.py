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
text = "man ran fan ñam ban omniman"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)

print("\n")

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban.
text = "omniman fanatico man bandana man fan ban"
pattern = r"\b[mfb]an\b" # ? La barra invertida \b indica el inicio o el final de una palabra.
matches = re.findall(pattern, text)
print(matches)


# Ejercicio con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png
# Buscar corner cases que no pasa y arreglarlo:
# Validación de correo electrónico usando Regex
emails = [
    "lo.que+sea@shopping.online",
    "michael@gov.co.uk",
    "usuario@dominio.com",
    "invalido@dominio",
    "otro+ejemplo@sub.dominio.org"
]

# Este patrón es una expresión regular para validar direcciones de correo electrónico.
# Desglose:
# ^                  : Indica el inicio de la cadena.
# [\w\.\+\-]+        : Uno o más caracteres que pueden ser letras, números, guion bajo (_), punto (.), más (+) o guion (-).
#                      Esto representa la parte local del correo (antes del @).
# @                  : El carácter arroba obligatorio.
# ([\w\-]+\.)+       : Uno o más grupos de caracteres (letras, números, guion bajo o guion) seguidos de un punto.
#                      Esto permite subdominios y el dominio principal (por ejemplo, correo@sub.dominio.com).
# [a-zA-Z]{2,}       : Al menos dos letras (mayúsculas o minúsculas) para la extensión del dominio (.com, .es, etc.).
# $                  : Indica el final de la cadena.
pattern = r"^[\w\.\+\-]+@([\w\-]+\.)+[a-zA-Z]{2,}$"

for email in emails:
    if re.fullmatch(pattern, email):
        print(f"Correo válido: {email}")
    else:
        print(f"Correo inválido: {email}")

# ? El vibe coding me está consumiendo. Me agrada.

print("\n")

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola Mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)