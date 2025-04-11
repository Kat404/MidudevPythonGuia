# ---> Curso de Python de Midudev <---
# ! Módulo 3 - Clase 1 - Bucles while (01_loop_while.py)
# * Los bucles 'while' permiten ejecutar un bloque de código repetidamente mientras una condición específica sea verdadera.
# * Se utilizan cuando no se sabe de antemano cuántas veces se necesita repetir el código.
# ? Son fundamentales para crear programas que reaccionan a entradas cambiantes o que procesan datos hasta cumplir un criterio.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

print("\nBucles while:")

# * Bucle con una simple condición
contador = 0  # Inicializa la variable contador a 0

while contador <= 5:  # Mientras contador sea menor o igual a 5
    print(contador)  # Imprime el valor actual de contador
    contador += 1 # ? Es importante para evitar un bucle infinito # Incrementa contador en 1


# * Utiilizando la palabra 'break', para romper el bucle

print("\nBucle while con break:")
contador = 0  # Reinicia contador a 0

while contador <= 100:  # Mientras contador sea menor o igual a 100
    contador += 1  # Incrementa contador en 1
    print(contador)  # Imprime el valor actual de contador
    if contador == 5:  # Si contador es igual a 5
        break # ? Sale del bucle # Termina el bucle inmediatamente

# * 'continue', lo que hace es saltar esa iteración en concreto y continuar con el bucle.
print("\nBucle con continue:")

contador = 0  # Reinicia contador a 0
while contador < 10:  # Mientras contador sea menor que 10
    contador += 1  # Incrementa contador en 1
    if contador % 2 == 0:  # Si contador es par
        continue  # Salta el resto del código en esta iteración y pasa a la siguiente
    # ? ⬇️ Una vez la ejecución llegue al 'continue' para hacia la próxima iteración sin importar el código que tengamos abajo.
    print(contador)  # Imprime el valor actual de contador (solo si es impar)


# * 'else', ¿esta condición cuándo se ejecuta?
print("\nBucle while con else:")

contador = 0  # Reinicia contador a 0
while contador < 5:  # Mientras contador sea menor que 5
    print(contador)  # Imprime el valor actual de contador
    contador += 1  # Incrementa contador en 1
else:  # Se ejecuta cuando la condición del while ya no es verdadera (el bucle termina normalmente)
    print("El bucle ha terminado.")  # Imprime un mensaje indicando que el bucle finalizó

# * Pedirle al usuario un número que tiene que ser positivo, si no, no se le deja pasar.
numero = -1  # Inicializa numero con un valor negativo para asegurar que el bucle se ejecute al menos una vez
while numero <= 0:  # Mientras numero sea menor o igual a 0
    numero = int(input("\nEscribe un número positivo: \n> "))  # Pide al usuario un número y lo convierte a entero
    if numero < 0:  # Si el número ingresado es negativo
        print("El número debe ser positivo, intenta de nuevo.")  # Imprime un mensaje de error

print(f"El número que has introducido es: {numero}.")  # Imprime el número positivo introducido por el usuario

numero = -1  # Reinicia numero a -1
while numero <= 0:  # Mientras numero sea menor o igual a 0
    try:  # Inicia un bloque para manejar posibles errores
        numero = int(input("\nEscribe un número positivo: \n> "))  # Pide al usuario un número y lo convierte a entero
        if numero < 0:  # Si el número ingresado es negativo
            print("El número debe ser positivo, intenta de nuevo.")  # Imprime un mensaje de error
    except:  # Si ocurre un error durante la ejecución del bloque try (ej: el usuario no introduce un número)
        print("El valor introducido no es un número, intenta de nuevo.")  # Imprime un mensaje de error

print(f"El número que has introducido es: {numero}.")  # Imprime el número positivo introducido por el usuario



###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 10  # Inicializa contador en 10
while contador <= 10:  # Mientras contador sea menor o igual a 10 (debería ser >= 1 para contar hacia atrás)
    print(contador)  # Imprime el valor actual de contador
    contador -= 1  # Decrementa contador en 1
    if contador == 0:  # Si contador llega a 0
        break  # Termina el bucle

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero = 1  # Inicializa numero en 1
suma_de_pares = 0  # Inicializa la suma de pares en 0

while numero <= 20:  # Mientras numero sea menor o igual a 20
    if numero % 2 == 0:  # Si numero es par
        suma_de_pares += numero  # Añade numero a la suma de pares
    numero += 1  # Incrementa numero en 1

print(f"La suma de los números pares del 1 al 20 es: {suma_de_pares}")  # Imprime la suma total de los números pares


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
numero = int(input("Introduce un número: \n> "))  # Pide al usuario un número y lo convierte a entero
factorial = 1  # Inicializa el factorial a 1
contador = 1  # Inicializa el contador a 1

while contador <= numero:  # Mientras contador sea menor o igual al número ingresado
    factorial *= contador  # Multiplica el factorial por el valor actual del contador
    contador += 1  # Incrementa el contador en 1

print(f"El factorial del número {numero} es: {factorial}.")  # Imprime el resultado del factorial

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
contraseña = ""  # Inicializa la variable contraseña como una cadena vacía
while len(contraseña) < 8:  # Mientras la longitud de la contraseña sea menor que 8
    contraseña = input("Ingresa una contraseña válida (de al menos 8 caracteres): \n> ")  # Pide al usuario la contraseña
    if len(contraseña) >= 8:  # Si la longitud de la contraseña es 8 o más
        print("Contraseña válida. Registrada.")  # Imprime un mensaje de validación


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input("Ingresa un número poositivo: \n> "))  # Pide al usuario un número y lo convierte a entero
multiplicador = 1  # Inicializa el multiplicador en 1

while multiplicador <= 10:  # Mientras el multiplicador sea menor o igual a 10
    resultado = numero * multiplicador  # Calcula el resultado de la multiplicación
    print(f"{numero} * {multiplicador} = {resultado}.")  # Imprime la línea de la tabla de multiplicar
    multiplicador += 1  # Incrementa el multiplicador en 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = int(input("Ingresa un número positivo N: \n> "))  # Pide al usuario un número N y lo convierte a entero
numero = 2  # Inicializa la variable numero en 2 (el primer número primo)

while numero <= n:  # Mientras numero sea menor o igual a N
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario # Bandera para indicar si el número actual es primo
  divisor = 2  # Inicializa el divisor en 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero # Mientras el cuadrado del divisor sea menor o igual al número
    if numero % divisor == 0:  # Si numero es divisible por el divisor actual
      es_primo = False  # Si encontramos un divisor, no es primo # Marca el número como no primo
      break  # Salimos del bucle interior # Termina el bucle interno ya que no es necesario seguir comprobando
    divisor += 1  # Incrementa el divisor en 1
  if es_primo:  # Si la bandera es_primo sigue siendo True después del bucle interno
    print(numero)  # Imprime el número primo

  numero += 1 # Incrementa numero en 1 para comprobar el siguiente