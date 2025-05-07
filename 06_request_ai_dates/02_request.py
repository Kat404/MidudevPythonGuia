# ---> Curso de Python de Midudev <---
# ! Módulo 6 - HTTP Requests y APIs - Clase 2 (02_request.py)
# * En este archivo, exploraremos el manejo de peticiones HTTP y APIs en Python.
# * Aprenderemos a realizar peticiones HTTP, manejar respuestas, y trabajar con APIs REST.
# ? El manejo de peticiones HTTP es fundamental para aplicaciones que necesitan interactuar con servicios web y APIs externas.

import os  # * Importamos el módulo 'os' para interactuar con el sistema operativo
os.system("cls")  # ! Limpia la pantalla de la consola (en Windows)

# ! import sys -> Importa el módulo 'sys' para interactuar con el sistema operativo
# ? print(sys.executable) -> Muestra la ruta del intérprete de Python

# Cómo hacer peticiones a API's con Python
# con y sin dependencias

# * 1.- Sin dependencias (díficil y sin dependencias)
import urllib.request # ? Importamos el módulo 'urllib.request' para hacer peticiones HTTP
import json # ? Importamos el módulo 'json' para manejar datos JSON

api_post = "https://jsonplaceholder.typicode.com/posts"

print("Sin dependencias:")
try:
    response = urllib.request.urlopen(api_post) # ? Hacemos una petición GET a la API
    data = response.read() # ? Leemos la respuesta
    json_data = json.loads(data.decode("utf-8")) # ? Convertimos la respuesta a JSON
    # print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e.reason}")

# * 2.- Con dependencias (fácil y con dependencias / requests)
import requests # ? Importamos el módulo 'requests' para hacer peticiones HTTP

print("\nGET:")
api_post = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_post)
response_json = response.json()
# print(json)

# * 3.- POST
print("\nPOST:")
try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={
            "title": "Dirty Deeds Done Dirt Cheap",
            "body": "Stand",
            "userId": 1
        }
    )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
    
# * 4.- PUT
print("\nPUT:")
try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "title": "Scary Monsters",
            "body": "Stand",
            "userId": 1
        }
    )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
    
# Usar la API de OpenAI
OPENAI_KEY = "sk--XXX"

import json
def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"  # URL de la API de OpenAI
    headers = {
        "Content-Type": "application/json",  # Tipo de contenido de la petición
        "Authorization": f"Bearer {api_key}"  # Token de autenticación
    }
    data = {
        "model": "gpt-3.5-turbo",  # Modelo de lenguaje a utilizar
        "messages": [
            {
                "role": "user",
                "content": prompt  # Texto de la pregunta
            }
        ]
    }
    try:
        response = requests.post(url, json=data, headers=headers)  # Hacemos la petición
        response.raise_for_status()  # Lanzamos una excepción si hay error HTTP
        return response.json()  # Devolvemos la respuesta en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a OpenAI: {e}")  # Mostramos el error
        return None  # Devolvemos None si hay error

api_response = call_openai_gpt(OPENAI_KEY, "Hola, ¿cómo estás?")

if api_response:
    try:
        print("\nRespuesta de OpenAI:")
        print(api_response["choices"][0]["message"]["content"])  # Mostramos la respuesta
    except KeyError as e:
        print(f"Error en la estructura de la respuesta: {e}")  # Mostramos el error
        print("\nRespuesta completa:")  # Mostramos la respuesta completa
        print(json.dumps(api_response, indent=2))  # Mostramos la respuesta completa en formato JSON