from PIL import Image
import numpy as np

# para ello usaremos la libreria requests
import requests

# Implementaremos la libreria de matplotlib para poder graficar
import matplotlib.pyplot as plt

# Implementaremos la libreria matplotlib image para poder mostrar imagenes
import matplotlib.image as img


# Crearemos una variable pere pedirle informacion al usuario
pokemon = input("Ingrese el nombre del pokemon: ")

# Concatena la url con el pokemon que el usuario ingreso
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

# La variable pokemon tendra la informacion que nos devuelva la api
res = requests.get(url)

# Si el pokemon no existe nos devolvera un 404
if res.status_code != 200:
    print("Ese pokemon no existe :(")
    # Si el pokemon no existe salimos del programa para romper el ciclo if
    exit()

# Mostramos la imagen
imagen = res.json()["sprites"]["front_default"]

# Mostramos el nombre del pokemon
plt.title(pokemon)

# Mostramos la imagen
imagen_muestro = Image.open(requests.get(imagen, stream=True).raw)

# Mostramos la imagen con los datos originales
imgplot = plt.imshow(imagen_muestro)


# Mostramos los resultados
plt.show()