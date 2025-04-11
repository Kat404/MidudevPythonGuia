# ---> Curso de Python de Midudev <---
# ! Módulo 1 - Clase 3 - Conversión de Tipos (03_cast.py)
# * En Python, podemos cambiar el tipo de dato de una variable (casting).
# * Funciones como int(), float(), str(), bool() se usan para esto.

print("Conversión de tipos de datos:")
print(type(int("100"))) # Convierte la cadena "100" a entero y muestra su tipo: <class 'int'>


# La función round() redondea un número al entero más cercano
# Si el número está exactamente a la mitad entre dos enteros, 
# Python redondea al entero par más cercano (redondeo bancario)
print(round(2.5))  # Redondea 2.5 a 2 (redondeo al par más cercano)
print(round(3.5))  # Redondea 3.5 a 4 (redondeo al par más cercano)


print(int(2.5)) # Convierte el flotante 2.5 a entero (trunca decimales): 2
print(int(-2.5)) # Convierte el flotante -2.5 a entero (trunca decimales): -2
print(int("100") + 2) # Convierte "100" a entero y suma 2: 102
print(("100" + str(2))) # Convierte el entero 2 a cadena y concatena: "1002"

print(type(float(3.1416))) # Muestra el tipo del flotante 3.1416: <class 'float'>
print(float(3.1416)) # Muestra el valor flotante: 3.1416

print(bool(1)) # Convierte el entero 1 a booleano: True
print(bool(0)) # Convierte el entero 0 a booleano: False
print(bool(-1)) # Convierte el entero -1 a booleano: True (cualquier número distinto de 0 es True)

print(bool("")) # Convierte una cadena vacía a booleano: False
print(bool(" ")) # Convierte una cadena con espacio a booleano: True (cadena no vacía)
print(bool("False")) # Convierte la cadena "False" a booleano: True (cadena no vacía)

