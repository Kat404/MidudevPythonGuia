# ---> Curso de Python de Midudev <---
# ! Módulo 1 - Clase 5 - Entrada de Datos (05_input.py)
# * En Python, podemos recibir datos del usuario durante la ejecución mediante input().
# * La función input() siempre devuelve un string, por lo que debemos convertirlo si necesitamos otro tipo.

# El 'input' pregunta al usuario un valor y espera hasta que este ingrese algo
nombre: str = input('Bienvenido, ¿cuál es tu nombre?: \n> ') # \n crea una nueva línea, sin este salto de línea el input se imprimiría en la misma línea que el prompt.
print(f"Hola, {nombre}! Encantado de conocerte.")

age: int = int(input('¿Cuántos años tienes? \n> '))
print(f"Dentro de 20 años tendrás {age + 20} años.")

print("Obtener múltiples datos en una línea:")
country, city = input('¿En qué país y ciudad vives? \n> ').split()

print(f"Vives en {country}, {city}.")
