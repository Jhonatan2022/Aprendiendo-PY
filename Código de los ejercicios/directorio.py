# Importar el módulo os para poder usar la función scandir
import os

# Directorio de ejemplo
ejemplo_dir = '/Users/JHONATAN FLOREZ/Documents/Curso python Bootcam/Ejercicios/'

# Usamos la función scandir para obtener un iterador de los archivos
with os.scandir(ejemplo_dir) as ficheros:

    # Ciclo for para imprimir los nombres de los archivos
    for fichero in ficheros:
        
        # Imprimimos el nombre del archivo
        print(fichero.name)