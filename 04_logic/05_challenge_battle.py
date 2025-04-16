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
    # Crear copias para no modificar las listas originales
    a = lista_a.copy()
    b = lista_b.copy()
    
    # Recorrer las listas hasta el penúltimo elemento
    for i in range(len(a) - 1):
        # Si hay empate, no se hace nada con el siguiente número
        if a[i] == b[i]:
            continue
            
        # Si gana a[i], su valor se suma al siguiente número en a
        if a[i] > b[i]:
            a[i + 1] = a[i + 1] + a[i]
            
        # Si gana b[i], su valor se suma al siguiente número en b
        elif b[i] > a[i]:
            b[i + 1] = b[i + 1] + b[i]
    
    # Comparación final
    if a[-1] > b[-1]:
        return f"{a[-1]}a"
    elif b[-1] > a[-1]:
        return f"{b[-1]}b"
    return "x"

# Casos de prueba
lista_a = [2, 4, 2]
lista_b = [3, 3, 4]
print(battle(lista_a, lista_b))  # Debe imprimir: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]
print(battle(lista_a, lista_b))  # Debe imprimir: "x"