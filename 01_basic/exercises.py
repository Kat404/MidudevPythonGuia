###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
# Solución: Usamos el carácter '\n' para crear un salto de línea entre el nombre y la ciudad.
# El '\n' es un carácter especial que significa "nueva línea".
print("Jose Luis,\nCiudad de México")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
# Solución: Usamos la función type() para mostrar el tipo de cada variable.
# La función type() devuelve la clase o tipo de dato de su argumento.
print("Tipo de dato de a:", type(a))  # <class 'int'> - a es un entero (int)
print("Tipo de dato de b:", type(b))  # <class 'float'> - b es un número decimal (float)
print("Tipo de dato de c:", type(c))  # <class 'str'> - c es una cadena de texto (str)
print("Tipo de dato de d:", type(d))  # <class 'bool'> - d es un valor booleano (bool)
print("Tipo de dato de e:", type(e))  # <class 'NoneType'> - e es None (NoneType)

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
# Solución: Usamos las funciones int() y float() para convertir entre tipos.
# Primero convertimos la cadena "12345" a entero usando int()
numero = print(int("12345"))  # Imprime: 12345 (como entero)

# Luego convertimos la cadena "12345" directamente a float usando float()
numero = print(float("12345"))  # Imprime: 12345.0 (como flotante)

# Convertimos la cadena "3.99" a float
numero = print(float("3.99"))  # Imprime: 3.99 (como flotante)

# Convertimos el número 3.99 a entero
# Al convertir float a int, Python trunca el valor (elimina la parte decimal)
numero = print(int(3.99))  # Imprime: 3 (se pierde la parte decimal - trunca, no redondea)

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
# Solución: Creamos tres variables y usamos f-strings para insertar sus valores en una cadena.
# Las f-strings permiten insertar variables y expresiones directamente en cadenas de texto.
name = "Jose"  # Variable para el nombre
age = 19       # Variable para la edad
height = 1.71  # Variable para la altura
print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros.")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Solución:
# 1. Creamos una variable con una aproximación del número PI
PI = 3.14159
print(PI)  # Imprime el valor de PI: 3.14159

# 2. Usamos round() para redondear PI al entero más cercano
print(round(PI))  # Imprime: 3 (PI redondeado)

# 3. Realizamos la división entera de PI entre 2 usando el operador //
# La división entera devuelve solo la parte entera del resultado (trunca el decimal)
print(PI // 2)  # Imprime: 1 (3.14159 // 2 = 1.57... pero se trunca a 1)
