# ---> Curso de Python de Midudev <---
# ! Módulo 1 - Clase 1 - Básicos de Python (01_print.py)
# * El módulo print() es una función que se utiliza para imprimir mensajes en la consola.
# * Sirve para imprimir mensajes en la consola, es decir, para mostrar información al usuario.
# ? Lo vamos a usar siempre, desde el principio de nuestro aprendizaje hasta el final.
# Imprime "Hola Mundo" en la consola
print("Hola Mundo")

# Imprime "Python es genial" en la consola, separando cada palabra con un espacio por defecto
print("Python", "es", "genial")

# Imprime "Python-es-brutal" en la consola, usando "-" como separador entre palabras
print("Python", "es", "brutal", sep="-")

# Estos dos print juntos imprimen "Esto se imprime en la misma línea"
# El parámetro end=" " reemplaza el salto de línea por un espacio
print("Esto se imprime", end=" ")
print("en la misma línea")

# Estos dos print juntos imprimen "Hola Mundo"
# El primer print termina con un espacio en lugar de un salto de línea
print("Hola", end=" ")
print("Mundo")

# Estos dos print juntos imprimen "Hola!Mundo"
# El primer print termina con "!" en lugar de un salto de línea
print("Hola", end="!")
print("Mundo")

# Imprime el número 42 en la consola
print(42)