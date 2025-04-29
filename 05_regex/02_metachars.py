# ---> Curso de Python de Midudev <---
# ! Módulo 5 - Meta caracteres - Clase 2 (02_metachars.py)
# * En este archivo, profundizaremos en los metacaracteres de las expresiones regulares (regex) en Python.
# * Los metacaracteres permiten crear patrones más complejos y potentes para buscar, validar y manipular texto.
# ? Comprender los metacaracteres es clave para dominar las regex y resolver problemas avanzados de procesamiento de texto.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
import re # * Importamos el módulo 're' para interactuar con el sistema regex
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# * El punto (.)
# * Coincidir con cualquier caracter excepto una nueva línea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # ? Hola, H0la

found = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto

if (found):  # Si se encontraron coincidencias
    print(found)  # Imprime las coincidencias
else:  # Si no se encontraron coincidencias
    print("No se ha encontrado el patrón en el texto.")  # Imprime mensaje de no encontrado


text = "casa caasa cosa cisa cesa causa"  # Cadena de texto de ejemplo
pattern = "c.sa"  # Patrón regex: c seguido de cualquier caracter y luego sa

matches = re.findall(pattern, text)  # Busca todas las coincidencias del patrón en el texto
print(matches)  # Imprime las coincidencias

# --------------------------------------------------------------------------------------------------------
print("\n")

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # ? Hola, H0la
# ? La 'r' se utiliza para definir que lo siguiente va a ser una expresión regular.

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patrón en el texto.")
print("\n")

# * Cómo usar la barra invertida (\) para anular el significado especial de un símbolo.
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\." 
# ? El punto es un valor especial ya que expresa cualquier caracter y por eso se imprime toda la frase junto con los espacios.

matches = re.findall(pattern, text)
print(matches)

# * \d: Coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{9}', text)

print(found)

# * Ejercicio: Detectar si hay un número de México en el texto gracias al prefijo +52

text = "Mi número de teléfono es +52 8352039475 anótale ok?"
pattern = r"\+52 \d{10}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}.")

# * \w: Coincide con cualquier caracter alfanumérico (a-z, A-Z, 0-9, ...)
text = "@@@!el_rubius_69)/&"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

print("\n")

# * \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

print("\n")

# * ^: Coincide con el principio de una cadena
username = "248_name%99"
pattern = r"^\w" # Validar nombre de usuario asegurándose de que empiece con un caracter alfanumérico

valid = re.search(pattern, username)
if valid: print("El nombre es válido.")
else: print("El nombre de usuario no es válido.")

phone = "+52 9472937586"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido.")
else: print("El número de teléfono no es válido.")

print("\n")

# * $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$" # ? Coincide con el final de la cadena

valid = re.search(pattern, text)
if valid: print("La cadena es válida.")
else: print("La cadena no es válida.")

# EJERCICIO: Valida que un correo sea de gmail
text = "xocechernov@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es un gmail válido.")
else: print("El correo no es un gmail válido.")

print("\n")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos los nombres de los ficheros con extensiones .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w+\.txt\b"
# ? Tuve que apoyarme de IA para poder encontrar una solución, modo usado -> Ask

valid = re.findall(pattern, files)
if valid: print(valid)
else: print("No se ha encontrado ningún archivo .txt")

print("\n")

# * \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

print("\n")

# * |: Coincidir con una opción u otra
fruits = "platano, sandia, melon, pera, manzana, aguacate, pera"
pattern = r"aguacate|pera|m...n|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)