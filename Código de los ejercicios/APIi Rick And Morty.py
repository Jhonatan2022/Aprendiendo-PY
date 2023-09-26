import requests
import matplotlib.pyplot as plt

# Hacemos una petición a la API de Rick and Morty para obtener la información del personaje
num = input("Ingrese un número: ")

# Hacemos una petición a la API de Rick and Morty para obtener la información del personaje
response = requests.get(f"https://rickandmortyapi.com/api/character/{num}")

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
data = response.json()

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
name = data["name"]

# Extraemos el nombre del personaje y la URL de la imagen de la respuesta de la API
image_url = data["image"]

# Descargamos la imagen utilizando la librería requests
response = requests.get(image_url)

# Guardamos la imagen en un archivo
with open(f"{name}.jpg", "wb") as f:
    # Escribimos la imagen en el archivo
    f.write(response.content)


# Mostramos la imagen utilizando la librería matplotlib
image = plt.imread(f"{name}.jpg")

# Mostramos la imagen utilizando la librería matplotlib
plt.imshow(image)

# Mostramos el nombre del personaje
plt.title(name)

# Ocultamos los ejes
plt.axis("off")

# Mostramos la imagen
plt.show()
