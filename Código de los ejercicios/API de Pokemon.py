# hola gente de youtube
# Implementaremos una api de pokemon https://pokeapi.co/api/v2/pokemon/


from PIL import Image
import numpy as np
# para ello usaremos la libreria requests
import requests
# Implementaremos la libreria de matplotlib para poder graficar
import matplotlib.pyplot as plt
# Implementaremos la libreria matplotlib image para poder mostrar imagenes
import matplotlib.image as img


# Crearemos una variable pere pedirle informacion al usuario
pokemon = input('Ingrese el nombre del pokemon: ')

# Crearemos una variable para poder usar la api de pokemon debemos usar la url de la api
# Concatena la url con el pokemon que el usuario ingreso
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

# Creamos una variable para poder hacer la peticion a la api
# Usamos el metodo get de la libreria requests
# Le pasamos como parametro la url
# La variable pokemon tendra la informacion que nos devuelva la api
res = requests.get(url)

# Implementamos un if para ver si el pokemon existe
# Si el pokemon existe nos devolvera un 200
# Si el pokemon no existe nos devolvera un 404
if res.status_code != 200:
    print('Ese pokemon no existe :(')
    # Si el pokemon no existe salimos del programa para romper el ciclo if
    exit()

# Mostramos la imagen del pokemon que ingreso el usuario
# Usamos la libreria matplotlib image
# Le pasamos como parametro la url de la imagen
# Le pasamos como parametro la imagen
# Mostramos la imagen
imagen = res.json()['sprites']['front_default']

# Obtendremos el nombre del pokemon que ingreso el usuario
# Usamos la libreria matplotlib
# Le pasamos como parametro el nombre del pokemon
# Mostramos el nombre del pokemon
plt.title(pokemon)

# Mostramos la imagen del pokemon
# Usamos la libreria matplotlib
# Le pasamos como parametro la imagen
# Mostramos la imagen
imagen_muestro = Image.open(requests.get(imagen, stream=True).raw)

# Omitimos el pasar la imagen a un array para mantener la imagen original
# imagen_matriz = np.asarray(imagen_muestro)

# Mostramos la imagen con los datos originales
imgplot = plt.imshow(imagen_muestro)


# Mostramos los resultados en pantalla
# Mostramos los resultados
plt.show()
