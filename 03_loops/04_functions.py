# ---> Curso de Python de Midudev <---
# ! Módulo 3 - Clase 4 - Funciones (04_functions.py)
# * Las funciones son bloques de código reutilizables que realizan una tarea específica.
# * Se utilizan para organizar y estructurar el código, evitando la repetición.
# ? Son esenciales para escribir programas más claros, eficientes y fáciles de mantener.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la función
    return valor_de_retorno  # opcional
"""

# * Ejemplo de una función para imprimir algo en consola:
def saludar():
    print("¡Hola!")

saludar()  # ? Llamada a la función 'saludar' para ejecutar su código

# * Ejemplo de una función con parámetro
def saludar_a(nombre):
    print(f"Hola {nombre}!")

saludar_a("Midudev")  # ? Llamada a la función 'saludar_a' con el argumento "Midudev"
saludar_a("Papá")  # ? Llamada a la función 'saludar_a' con el argumento "Papá"
saludar_a("Mamá")  # ? Llamada a la función 'saludar_a' con el argumento "Mamá"
saludar_a("Hermano")  # ? Llamada a la función 'saludar_a' con el argumento "Hermano"
saludar_a("Hermana")  # ? Llamada a la función 'saludar_a' con el argumento "Hermana"

# ? El parámetros es lo que acepta la función
# ? EL argumento es lo que se le pasa a la función

# * Funciones con más parámetros
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    suma = a + b
    return suma

result = (sumar(2, 3))  # ? Llamada a la función 'sumar' con los argumentos 2 y 3
print(result)

# * Documentar las funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve el resultado.""" # ? Muestra la documentación de la función 'restar' en consola
    return a - b

# help(restar)  # ? Muestra la documentación de la función 'restar' en consola

# * Parámetros por defecto
def multiplicar (a, b = 2):
    """Multiplica dos números y devuelve el resultado.""" # ? Muestra la documentación de la función 'multiplicar' en consola
    return a * b

print(multiplicar(2)) # ? Llamada a la función 'multiplicar' con el argumento 2 y el parámetro b por defecto (2)
print(multiplicar(2, 3)) # ? Llamada a la función 'multiplicar' con los argumentos 2 y 3

# * Argumentos por posición

def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}.")

# ? Los parámetros son posicionales (por el orden en el que se colocan los datos).
describir_persona("Jose", 19, "hombre")  # ? Llamada a la función 'describir_persona' con los argumentos "Jose", 19 y "hombre"
describir_persona("hombre", "Juan", 20) # ! El problema es que no se puede cambiar el orden de los argumentos.

# * Argumentos por clave
# * Parámetros nombrados
describir_persona(sexo = "hombre", nombre = "José", edad = 19) # ? Llamada a la función 'describir_persona' con los argumentos "hombre", "José" y 19.

# * Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))  # ? Llamada a la función 'sumar_numeros' con los argumentos 1, 2, 3, 4 y 5.
print(sumar_numeros(1, 2))  # ? Llamada a la función 'sumar_numeros' con los argumentos 1 y 2.
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # ? Llamada a la función 'sumar_numeros' con los argumentos 1, 2, 3, 4, 5, 6, 7, 8, 9 y 10.

# * Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):  # ? Define una función que acepta argumentos de clave-valor variables.
    for clave, valor in kwargs.items():  # ? Itera sobre cada par clave-valor en los argumentos.
        print(f"{clave}: {valor}")  # ? Imprime la clave y su valor en formato "clave: valor".

# ? Se pueden usar diferentes variables al momento de usar **kwargs
# ? Como: nombre, nickname, name, etc...
mostrar_informacion_de(nombre="José", edad=19, sexo="hombre")  # ? Llamada a la función 'mostrar_informacion_de' con los argumentos "nombre", "edad" y "sexo".
print("\n")  # ? Salto de línea para separar la salida de las funciones
mostrar_informacion_de(nombre="Juan", edad=22, country="Argentina")  # ? Llamada a la función 'mostrar_informacion_de' con los argumentos "nombre", "edad" y "sexo".
print("\n")  # ? Salto de línea para separar la salida de las funciones
mostrar_informacion_de(nombre="Pedro", edad=35, is_student=True, is_bilingual=False)  # ? Llamada a la función 'mostrar_informacion_de' con los argumentos "nombre", "edad" y "sexo".
print("\n")  # ? Salto de línea para separar la salida de las funciones
mostrar_informacion_de(nombre="Jesús", edad=30, country="Jerusalén", sexo="hombre")

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
def imprimir_numeros_del_1_al_10():
    for numero in range(1, 11):
        print(numero)

imprimir_numeros_del_1_al_10()

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
def imprimir_numeros_impares_del_1_al_20():
    for numero in range(1, 21, 2):
        print(numero)

imprimir_numeros_impares_del_1_al_20()

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
def imprimir_multiplos_de_5():
    for numero in range(5, 51, 5):
        print(numero)

imprimir_multiplos_de_5()

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
def imprimir_numeros_en_orden_inverso():
    for numero in range(10, 0, -1):
        print(numero)

imprimir_numeros_en_orden_inverso()

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
def sumar_numeros_del_1_al_100():
    suma = 0
    for numero in range(1, 101):
        suma += numero
    return suma

print(sumar_numeros_del_1_al_100())

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
def imprimir_tabla_de_multiplicar():
    numero = int(input("Introduce un número para ver su tabla de multiplicar: \n> "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

imprimir_tabla_de_multiplicar()