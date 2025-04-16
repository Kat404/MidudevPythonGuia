# ---> Curso de Python de Midudev <---
# ! Módulo 4 - Lógica - Ejercicio 3 (03_challenge_find_first_sum.py)
# * En este módulo, nos centraremos en resolver problemas de lógica utilizando Python.
# * Estos ejercicios ayudan a desarrollar el pensamiento algorítmico y la capacidad de resolver problemas.
# ? La lógica de programación es fundamental para construir aplicaciones complejas y eficientes.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

"""
def find_first_sum(nums, goal):
    # ? early return, una validación rápida para evitar recorrer todo el array.
    if len(nums) == 0:
        return None # ? Si el array está vacío, no hay nada que recorrer.

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]
    return None # ? No se encontró ninguna combinación que sumen el número goal.
"""

def find_first_sum(nums, goal):
    seen = {} # ? Diccionario para guardar el número y su índice.

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        
        seen[value] = index # ? Guardar el número actual a los vistos, porque no hemos encontrado

    return None

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) # ? [2, 3]
print(result)

