import requests
import matplotlib.pyplot as plt
from urllib.request import urlopen

# Hacemos una petición a la API de Rick and Morty para obtener la información del personaje
num = input("Ingrese el número del personaje: ")

# Hacemos una petición a la API de Rick and Morty para obtener la información del personaje
response = requests.get(f"https://rickandmortyapi.com/api/character/{num}")

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
data = response.json()

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
name = data["name"]

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
image_url = data["image"]


# Leemos la imagen desde la URL utilizando la librería urllib.request
with urlopen(image_url) as url:

    # Guardamos la imagen en un archivo
    image = plt.imread(url, format='jpg')

# Mostramos la imagen utilizando la librería matplotlib
plt.imshow(image)

# Mostramos el nombre del personaje
plt.title(name)

# Ocultamos los ejes
plt.axis("off")

# Mostramos la imagen
plt.show()