# Mover archivos de un lugar a otro con python
import shutil

# Digitamos la ruta origen de nuestros archivos
rutaorigen = "/Users/JHONATAN FLOREZ/Downloads/PYTHON/Turtle python/"

# Digitamos la ruta destino de nuestros archivos
rutadestino = "/Users/JHONATAN FLOREZ/Downloads/PYTHON/"

# Digitamos los nombres de nuestros archivos a mover
shutil.move(rutaorigen + "README.md", rutadestino)