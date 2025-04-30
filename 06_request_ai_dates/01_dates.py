# ---> Curso de Python de Midudev <---
# ! Módulo 6 - Fechas y Tiempo - Clase 1 (01_dates.py)
# * En este archivo, exploraremos el manejo de fechas y tiempos en Python.
# * Aprenderemos a trabajar con objetos datetime, formatear fechas, y realizar operaciones con fechas y horas.
# ? El manejo de fechas es fundamental para aplicaciones que requieren registro de eventos, cálculos temporales y manejo de zonas horarias.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
from datetime import datetime, timedelta  # * Importamos datetime y timdelta como 'datetime'
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # ? Obtiene los datos locales y los utiliza
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# * 1.- Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# * 2.- Crear una fecha y hora específica
specific_date = datetime(2025, 9, 19)
print(f"Fecha y hora específica de mi cumpleaños: {specific_date}")

# * 3.- Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el fomato especificado
# formato:
format_date = now.strftime("%A %B %Y %H:%M:%S") # ? Los símbolos entre las fechas pueden ser cualquiera y se van a imprimar como tal.
print(f"Fecha formateada: {format_date}")

# * 4.- Operaciones con fechas (sumar/restar días, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1) # ? También es posible sumar o resta mediodía (days=0.5)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# * 5.- Obtener componentes individuales de una fecha
year = now.year
print(f"Año actual: {year}")

month = now.month
print(f"Mes actual: {month}")

# * 6.- Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2024, 12, 8, 16, 24, 41)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")