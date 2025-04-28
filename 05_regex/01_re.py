# ---> Curso de Python de Midudev <---
# ! Módulo 5 - Expresiones Regulares - Clase 1 (01_re.py)
# * En este módulo, nos centraremos en aprender y practicar expresiones regulares (regex) utilizando Python.
# * Las expresiones regulares son herramientas poderosas para buscar, validar y manipular cadenas de texto.
# ? Dominar las regex es fundamental para el procesamiento de datos, validación de formularios y muchas tareas de programación.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

""" ¿Por qué aprender Regex?
-> Las expresiones regulares son una herramienta poderosa para trabajar con texto.
-> Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)
-> Asegurarte que los datos que ingresa un usuario con el email, teléfono, etc. son correctos.
-> Extraer, reemplazar y moidificar partes de la cadena de texto fácilmente.
"""

# ? 1.- Importar el módulo de expresiones regulares 're'.
import re  # * Importamos el módulo 're' que proporciona funciones para trabajar con expresiones regulares en Python.
# ? 2.- Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar.
pattern = "Hola"  # * Definimos un patrón simple que buscamos en una cadena de texto.
# ? 3.- El texto donde queremos buscar.
text = "Hola Mundo"  # * Definimos una cadena de texto donde buscaremos el patrón.
# ? 4.- Usar la función de búsqueda de 're'.
result = re.search(pattern, text) # * Usamos la función 'search' del módulo 're' para buscar el patrón en el texto.

if result:
    print("He encontrado el patrón en el texto.")
else:
    print("No he encontrado el patrón en el texto.")

print(result.group())  # * Si se encuentra el patrón, usamos 'group()' para obtener el texto que coincide con el patrón.

print(result.start())  # * Usamos 'start()' para obtener la posición inicial de la coincidencia en el texto.

print(result.end())  # * Usamos 'end()' para obtener la posición final de la coincidencia en el texto.

""" Ejercicio 1:
Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto.
E indica en que posición se empieza y termina la coincidencia. 
"""

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

found_ia = re.search(pattern, text)
if found_ia:
    print("He encontrado el patrón en el texto.")
    print(f"El patrón empieza en la posición {found_ia.start()} y termina en la posición {found_ia.end()}.")
else:
    print("No he encontrado el patrón en el texto.")

# --------------------------------------------------------------------------------------------------------------
# * Encontrar todas las coincidencias de un patrón en un texto.
# * .findall() devuelve una lista con todas las coincidencias encontradas.

text = "Me gusta Python. Python es muy chido. Aunque Python no es tan díficil como Java, prefiero Python."
pattern = "Python"

matches = re.findall(pattern, text)  # * Usamos 'findall' para encontrar todas las coincidencias del patrón en el texto.
print(len(matches))  # * Imprimimos la lista de coincidencias encontradas.

# --------------------------------------------------------------------------------------------------------------
# * iter() devuelve un iterador que contiene los resultados de la búsqueda.

text = "Me gusta Python. Python es muy chido. Aunque Python no es tan díficil como Java, prefiero Python."
pattern = "Python"

matches = re.finditer(pattern, text)  # * Usamos 'findall' para encontrar todas las coincidencias del patrón en el texto.

for match in matches:
    print(match.group(), match.start(), match.end())  # * Imprimimos cada coincidencia encontrada, junto con su posición inicial y final.


# * Ejercicio 2:
# * Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en qué posición se empieza y termina cada coincidencia y cuántas veces se encontró.

# Definimos el texto donde buscaremos el patrón
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu."
# Definimos el patrón a buscar
pattern = "midu"

# Usamos finditer() para encontrar todas las ocurrencias del patrón
matches_midu = re.finditer(pattern, text)

# Iteramos sobre cada coincidencia encontrada
for match in matches_midu:
    # Imprimimos el texto encontrado y sus posiciones de inicio y fin
    print(match.group(), match.start(), match.end())

# ----------------------------------------------------------------------------------------------------------------------
print("\n")
# * Modificadores
# * Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento.
# * re.IGNORECASE: Ignora las mayúsculas y minúsculas al buscar.

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"

found = re.findall(pattern, text, re.IGNORECASE) # ? El IGNORECASE hará que se ignore entre mayúsculas y minúsculas en el patrón -> texto.

if found: print(found)
if found:
    print(f"He encontrado el patrón {found} en el texto.")
    print(f"Se encontró {len(found)} veces.")
else:
    print("No he encontrado el patrón en el texto.")

print("\n")

# * Ejercicio 3
# * Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)
if found:
    print(f"He encontrado el patrón {found} en el texto.")
    print(f"Se encontró {len(found)} veces.")
else:
    print("No he encontrado el patrón en el texto.")

print("\n")
# ------------------------------------------------------------------------------------------------------------------------------------
# * Reemplazar el texto
# * .sub() reemplaza todas las coincidencias de un patrón en un texto.

text = "Hola, mundo! Hola de nuevo."
pattern = "Hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text)
print(new_text)

"""
re.search
Busca la primera coincidencia del patrón en el texto y devuelve un objeto Match (o None si no hay coincidencia). Permite obtener la posición y el texto encontrado.

re.findall
Devuelve una lista con todas las coincidencias del patrón en el texto. Solo devuelve las cadenas encontradas, no objetos Match.

re.finditer
Devuelve un iterador de objetos Match para todas las coincidencias del patrón en el texto. Permite acceder a la posición y el texto de cada coincidencia.

search: primera coincidencia (objeto Match)
findall: todas las coincidencias (lista de strings)
finditer: todas las coincidencias (iterador de objetos Match)
"""