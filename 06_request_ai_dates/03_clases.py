# ---> Curso de Python de Midudev <---
# ! Módulo 6 - HTTP Requests y APIs - Clase 3 (03_clases.py)
# * En este archivo, exploraremos la programación orientada a objetos (POO) en Python.
# * Aprenderemos a crear y utilizar clases, así como los conceptos fundamentales de la POO.
# ? La POO es una forma poderosa de organizar el código que nos permite crear estructuras reutilizables y mantenibles.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# ! import sys -> Importa el módulo 'sys' para interactuar con el sistema operativo
# ? print(sys.executable) -> Muestra la ruta del intérprete de Python

# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar

OPENAI_KEY = ""
DEEPSEEK_KEY = ""

# Ejemplo básico de una clase
class Coche:
    # Atributo de clase (comparte todas las instancias)
    tipo = "Vehículo de cuatro ruedas"
    
    # Método especial que es el que construye el objeto
    # Se llama automáticamente este método cuando creas la instancia
    def __init__(self, marca, modelo, color):  # ? El self se refiere a sí mismo
        # Atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!")
         
mi_coche = Coche("Toyota", "Prius", "Negro")
mi_coche.arrancar()
print(mi_coche.marca)

coche_de_dima = Coche("Honda", "CR-V", "Gris métalico")
coche_de_dima.arrancar()
print(coche_de_dima.marca)
        
# ? Encapsulación: Es ocultar los detalles internos de una clase y exponer solo la interfaz pública.

# Crear una clase para llamar a la AI de OpenAI, DeepSeek o cualquier cosa
import requests

class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model
        
    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except:
            print(f"Error en la solicitud: {e}")
        return None
    
print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-3.5-turbo")
openai_api.call("Escribe un breve texto acerca de lo que es la programación")

print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")
deepseek_api.call("Escribe un breve texto acerca de lo que es la programación")