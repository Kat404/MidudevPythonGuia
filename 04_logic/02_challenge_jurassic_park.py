# ---> Curso de Python de Midudev <---
# ! Módulo 4 - Lógica - Ejercicio 2 (02_challenge_jurassic_park.py)
# * En este módulo, nos centraremos en resolver problemas de lógica utilizando Python.
# * Estos ejercicios ayudan a desarrollar el pensamiento algorítmico y la capacidad de resolver problemas.
# ? La lógica de programación es fundamental para construir aplicaciones complejas y eficientes.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)


"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# ? Para saber si un número es par, siempre usar el operador de módulo (%)
# ? Nos da el resto de la división entre dos números.
# ? Si el resto es 0, el número es par.
# ? Si el resto es 1, el número es impar.
def count_canivore_dinosaur_eggs(egg_list: list[int]) -> int:
    """
    Esta función recibe una lista de número enteros que representan la cantidad de huevos puestos por diferentes dinosaurios en el parque jurásico.
    Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.
    La función devuelve la suma total de los huevos que pertenecen a los dinosaurios carnívoros.
    """
    total_carnivore_eggs: int = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
        
    return total_carnivore_eggs

egg_list = [3, 4, 7, 5 ,8]
print(count_canivore_dinosaur_eggs(egg_list)) # ! 12
