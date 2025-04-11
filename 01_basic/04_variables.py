# ---> Curso de Python de Midudev <---
# ! Módulo 1 - Clase 4 - Variables y Tipado (04_variables.py)
# * En Python, las variables son contenedores para almacenar valores de datos.
# * Python no requiere declaración de tipos y las variables se crean al asignarles un valor. 
# * Python es un lenguaje de tipado dinámico y de tipado fuerte.

# Asignar una variable
# Solo hace falta hacer esto:
my_name = "Jose"
print(my_name)

age = 19
print(age)

age = 21
print(age)

# Tipado dinámico:
# El tipo de dato se determina en tiempo de ejecución.
# No es necesario declarar el tipo de dato de la variable.

name = "Jose"  # Inicialmente name contiene un string
print(type(name))  # Muestra: <class 'str'>

# El linter muestra error aquí porque al final del archivo hay una anotación name: str = "Jose"
# La anotación sugiere que name debería ser siempre str, pero Python ignora esto en tiempo de ejecución
# ? name = 19  # Cambiamos el tipo de str a int - el IDE marca error pero Python lo ejecuta sin problemas
print(type(name))  # Muestra: <class 'int'> - la variable cambió de tipo dinámicamente

# Tipado fuerte:
# Python no realiza conversiones de tipo automáticas.
# Disponible desde Python 3.5
# print("10" + 2) # ! Error: no se puede concatenar una cadena con un número

# f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age - 2} años.")

# No recomendada forma de asignar variables
name, age, city = "Jose", 19, "Mexico"

# Convenciones de nombres de variables
mi_nombre_de_variable = "OK" # Snake case
nombre = "OK" # Camel case

MiNombreDeVariable = "KO" # Pascal case
minombredevariable = "KO" # Camel case (todo junto)

mi_nombre_de_variable_123 = "OK" # Snake case

# ? Curiosidad: Las 'constantes' en Python no existen pero se puede usar UPPERCASE para indicar que es una constante y no cambiar su valor.
# ? Aunque dicho valor si se puede ser cambiado.
MI_CONSTANTE = 3.1416 # UPPERCASE --> constantes

# * Nombres no válidos de variables
# 12345_variable = "KO"  # ! Las variables no pueden comenzar con números
# mi-variable = "KO"     # ! Los guiones no están permitidos en nombres de variables
# mi variable = "KO"     # ! Los espacios no están permitidos en nombres de variables


# * Palabras reservadas
# True = False # ! No se puede usar palabras reservadas como nombres de variables
# ? Las palabras reservadas en Python son:
# and       as        assert    break     class     continue
# def       del       elif      else      except    finally
# for       from      global    if        import    in
# is        lambda    nonlocal  not       or        pass
# raise     return    try       while     with      yield

# * Tipado de datos
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
# ? Tipado dinámico:
# El tipo de dato se determina en tiempo de ejecución.
# No es necesario declarar el tipo de dato de la variable.
# ? Tipado fuerte:
# Python no realiza conversiones de tipo automáticas.

# Declaramos una variable con anotación de tipo 'bool'
is_user_logged_in: bool = True
print(is_user_logged_in)  # Imprime: True

"""
En Python, las anotaciones de tipo como ':bool' son solo sugerencias y no restricciones.
Estas anotaciones son útiles por varias razones:
1. Documentan el tipo esperado de la variable
2. Permiten a herramientas de análisis estático (como mypy o el IDE) detectar errores de tipo
3. Mejoran la legibilidad del código

Sin embargo, Python es un lenguaje de tipado dinámico, por lo que ignorará estas 
anotaciones en tiempo de ejecución y permitirá asignar cualquier tipo de valor.
"""

# Aunque declaramos que is_user_logged_in es de tipo bool, Python permite asignarle un entero
# ? is_user_logged_in = 42  # Un IDE o verificador de tipos mostrará un error, pero Python lo ejecutará sin problemas
print(is_user_logged_in)  # Imprime: 42

name: str = "Jose"
