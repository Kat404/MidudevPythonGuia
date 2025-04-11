# ---> Curso de Python de Midudev <---
# ! Módulo 1 - Clase 2 - Tipos de Datos (02_types.py)
# * Python tiene varios tipos de datos.
# * int, float, complex, str, bool, NoneType, list, tuple, dict, range, set, etc.

print("int:")
print(type(10))  # Muestra el tipo de dato del número 10: <class 'int'>
print(type(0))   # Muestra el tipo de dato del número 0: <class 'int'>
print(type(-10)) # Muestra el tipo de dato del número -10: <class 'int'>
print(type(9289572875967683948699846235867))  # Muestra el tipo de dato de un número entero muy grande: <class 'int'>
print(9289572875967683948699846235867)        # Imprime el valor del número entero grande: 9289572875967683948699846235867
print(9289572875967683948699846235867 + 1)    # Suma 1 al número entero grande y muestra el resultado: 9289572875967683948699846235868

print("float:")
print(type(3.14))  # Muestra el tipo de dato del número decimal 3.14: <class 'float'>
print(type(1.0))   # Muestra el tipo de dato del número decimal 1.0: <class 'float'>
print(type(1e3))   # Muestra el tipo de dato de la notación científica 1e3 (1000): <class 'float'>

print("complex:")
print(type(1 + 2j))  # Muestra el tipo de dato del número complejo 1+2j: <class 'complex'>

print("str:")
print(type("Hola"))  # Muestra el tipo de dato de la cadena "Hola": <class 'str'>
print(type(""))      # Muestra el tipo de dato de una cadena vacía: <class 'str'>
print(type("123"))   # Muestra el tipo de dato de la cadena "123" (no es un número): <class 'str'>
print(type("""
Multilinea
"""))               # Muestra el tipo de dato de una cadena multilínea: <class 'str'>

print("bool:")
print(type(True))    # Muestra el tipo de dato del valor booleano True: <class 'bool'>
print(type(False))   # Muestra el tipo de dato del valor booleano False: <class 'bool'>
print(type(1 < 2))   # Muestra el tipo de dato del resultado de la comparación 1<2 (True): <class 'bool'>

print("NoneType:")
print(type(None))    # Muestra el tipo de dato None (representa ausencia de valor): <class 'NoneType'>