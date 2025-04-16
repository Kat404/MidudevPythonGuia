# ---> Curso de Python de Midudev <---
# ! Módulo 4 - Lógica - Clase 4: Diccionarios (04_dictionaries.py)
# * En este módulo, exploramos diferentes estructuras de datos y conceptos lógicos en Python.
# * Los diccionarios son estructuras clave-valor fundamentales para organizar y acceder a datos.
# ? Comprender los diccionarios es esencial para manejar datos de forma eficiente.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# ? Ejemplo típico de diccionario
persona = {
    "nombre": "Jose Luis",
    "edad": 19,
    "es_estudiante": True,
    "calificaciones": [7, 5, 8],
    "socials": {
        "instagram": "jose_luis_dev",
        "linkedin": "jose_luis_dev",
        "github": "jose_luis_dev",
    }
}

# ? Para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["linkedin"])

# ? Cambiar valores al acceder
persona["nombre"] = "Juan"
persona["calificaciones"][1] = 10

# ? Eliminar completamente una propiedad
del persona["edad"] # ? El 'del' elimina la propiedad sin devolverla.
# print(persona)

# ? Podemos utilizar el 'pop' sin asignarla a una variable.
es_estudiante = persona.pop("es_estudiante") # ? El 'pop' elimina la propiedad y la devuelve.
print(f"es_estudiante: {es_estudiante}")
print(persona)

# ?  Sobreescrbir un diccionario con otro diccionario
a = { "name": "Jose Luis", "age": 19 }
b = { "name": "Juan", "es_estudiante": True }

a.update(b) # ? El 'update' actualiza el diccionario 'a' con los valores del diccionario 'b'.
print(a)

# ? Comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# ? Obtener todas las claves
print("\nKeys:")
print(persona.keys())

# ? Obtener todos los valores
print("\nValues:")
print(persona.values())

# ? Obtener todos los items (clave, valor)
print("\nItems:")
print(persona.items())


for key, value in persona.items():
    print(f"{key}: {value}")