# ---> Curso de Python de Midudev <---
# ! Módulo 2 - Clase 1 - Control de Flujo (01_if.py)
# * Las estructuras condicionales (if) permiten ejecutar código sólo si se cumple una condición.
# * Se utilizan para tomar decisiones en el programa basadas en valores de variables o expresiones.
# ? Son fundamentales para el control de flujo y la lógica de cualquier programa.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

print("\n Sentencia simple condicional")

edad = 18  # Definimos la variable 'edad' con valor 18
if edad >= 18:  # * Comprobamos si la edad es mayor o igual a 18
    print("Eres mayor de edad")  # Se ejecuta si la condición es verdadera
    print("Puedes votar y conducir.")  # También se ejecuta dentro del bloque if

edad = 16  # Redefinimos la variable 'edad' con valor 16
if edad >= 18:  # ? Comprobamos si la edad es mayor o igual a 18
    print("Eres mayor de edad")  # ! Este código no se ejecutará porque la condición es falsa
    print("Puedes votar y conducir.")  # ! Este código tampoco se ejecutará


print("\n Sentencia condicional con else")

edad = 16  # Definimos la variable 'edad' con valor 16
if edad >= 18:  # Comprobamos si la edad es mayor o igual a 18
    print("Eres mayor de edad")  # No se ejecuta porque la condición es falsa
else:  # * Se ejecuta cuando la condición del if es falsa
    print("Eres menor de edad")  # Se imprime este mensaje


print("\n Sentencia condicional con elif")

nota = 5  # Definimos la variable 'nota' con valor 5
if nota >= 9:  # Comprobamos si la nota es mayor o igual a 9
    print("¡Excelente!")  # No se ejecuta porque la condición es falsa
elif nota >= 7:  # * Si la primera condición es falsa, comprobamos si la nota es mayor o igual a 7
    print("Notable")  # No se ejecuta porque la condición es falsa
elif nota >= 6:  # * Si las anteriores condiciones son falsas, comprobamos si la nota es mayor o igual a 6
    print("Aprobado")  # No se ejecuta porque la condición es falsa
else:  # ! Se ejecuta cuando todas las condiciones anteriores son falsas
    print("Reprobado, estudia más.")  # Se imprime este mensaje

print("\n Condiciones múltiples")

edad = 16  # Definimos la variable 'edad' con valor 16
tiene_INE = True  # Definimos la variable 'tiene_INE' con valor True (verdadero)

# ? En un país normal y corriente...
if edad >= 18 and tiene_INE:  # * Comprobamos si la edad es mayor o igual a 18 Y tiene INE
    print("Puedes conducir!")  # No se ejecuta porque la primera parte de la condición es falsa
else:  # Se ejecuta cuando la condición del if es falsa
    print("No estás listo para la vida.")  # Se imprime este mensaje

print("\n")  # ? Imprime una línea en blanco como separador

# ? En un país diverso y algo raro...
if edad >= 18 or tiene_INE:  # * Comprobamos si la edad es mayor o igual a 18 O tiene INE
    print("Puedes conducir, asegúrate de no morir.")  # Se ejecuta porque tiene_INE es True
else:  # No se ejecuta porque la condición del if es verdadera
    print("Soborna al policía para poder conducir.")  # No se imprime este mensaje

es_fin_de_semana = False  # Definimos la variable 'es_fin_de_semana' con valor False (falso)
if not es_fin_de_semana:  # ! Comprobamos si NO es fin de semana (negación de la variable)
    print("¡A trabajar!")  # Se ejecuta porque la condición es verdadera

print("\n Anidar condicionales")

edad = 20  # Redefinimos la variable 'edad' con valor 20
tiene_dinero = True  # Definimos la variable 'tiene_dinero' con valor True (verdadero)

if edad >= 18:  # Comprobamos si la edad es mayor o igual a 18
    if tiene_dinero:  # * Si la primera condición es verdadera, comprobamos si tiene dinero
        print("¡Puedes salir de fiesta!")  # Se ejecuta porque ambas condiciones son verdaderas
    else:  # Se ejecutaría si tiene_dinero fuera False
        print("Será para la próxima.")  # No se ejecuta porque tiene_dinero es True
else:  # Se ejecutaría si edad < 18
    print("¡No puedes entrar!")  # No se ejecuta porque edad es 20

# Más sencillo:
# if edad < 18:
#     print("¡No puedes entrar!")
# elif tiene_dinero:
#     print("¡Puedes entrar a la fiesta!")
# else:
#     print("Quédate en casa.")

numero = 5
if numero: # True
    print("El número no es cero.")

numero = 0
if numero: # False
    print("Aquí no se ejecuta nunca.")

nombre = "Juan"
if nombre: # True
    print("El nombre no está vacío.")

numero = 3 # Asignación
es_el_tres = numero == 3 # Comparación
if es_el_tres:
    print("El número es 3")


print("\nLa condición ternaria:")
# * Es una forma concisa de un if-else en una sola línea de código.
# ? [código si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
# ó
print("Es mayor de edad" if edad >= 18 else "Es menor de edad")



###
# EJERCICIOS
###

print("\nEjercicios:")

print("\nEjercicio 1:")
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numero1 = int(input("Introduce el primer número: \n> "))
numero2 = int(input("Introduce el segundo número: \n> "))

if numero1 > numero2:
    print("El número mayor es:", numero1)
elif numero1 < numero2:
    print("El número mayor es:", numero2)
else:
    print("Los números son iguales")

print("\nEjercicio 2:")
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numero1 = int(input("Introduce el primer número: \n> "))
numero2 = int(input("Introduce el segundo número: \n> "))
operacion = input("Introduce la operación (+, -, *, /): \n> ")

resultado = None # ? Inicializamos resultado, ya que es necesario para poder imprimirlo.

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Error: División por cero.")
else:
    print("Operación no válida.")

if 'resultado' in locals():
    print(f'El resultado es: {resultado}')

print("\nEjercicio 3:")
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

año = int(input("Introduce un año: \n> "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")

print("\nEjercicio 4:")
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce tu edad: \n> "))

if edad >= 0 and edad <= 2:
    print("Eres un bebé.")
elif edad >= 3 and edad <= 12:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un adulto mayor.")
else:
    print("Edad no válida.")
