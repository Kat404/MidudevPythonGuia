# ---> Curso de Python de Midudev <---
# ! Módulo 4 - Lógica - Ejercicio 5 (05_challenge_battle.py)
# * En este módulo, nos centraremos en resolver problemas de lógica utilizando Python.
# * Estos ejercicios ayudan a desarrollar el pensamiento algorítmico y la capacidad de resolver problemas.
# ? La lógica de programación es fundamental para construir aplicaciones complejas y eficientes.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

# ? Se puede realizar de muchas formas
# ? Fuerza bruta: Hacer el buscando la solución manualmente, pero no es muy recomendable.
# ? Algortimos ocultos o cálculos o fórmulas.
# ? Programación dinámica: Buscar una solución más eficiente.

def battle(lista_a, lista_b):
    # Calcula la suma de todos los elementos en lista_a y la almacena en la variable puntos_a
    puntos_a = sum(lista_a)
    # Calcula la suma de todos los elementos en lista_b y la almacena en la variable puntos_b
    puntos_b = sum(lista_b)
    # Compara puntos_a y puntos_b para determinar el ganador
    # Si puntos_a es mayor que puntos_b, devuelve la diferencia seguida de "a"
    # Si puntos_b es mayor que puntos_a, devuelve la diferencia seguida de "b"
    # Si son iguales, devuelve "x"
    return f"{puntos_a - puntos_b}a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}b" if puntos_b > puntos_a else "x"

# Define la lista lista_a con los valores [4, 4, 4]
lista_a = [4, 4, 4]
# Define la lista lista_b con los valores [2, 8, 2]
lista_b = [2, 8, 2]
# Llama a la función battle con lista_a y lista_b, y guarda el resultado en la variable winner
winner = battle(lista_a, lista_b)
# Imprime el valor de la variable winner en la consola
print(winner)