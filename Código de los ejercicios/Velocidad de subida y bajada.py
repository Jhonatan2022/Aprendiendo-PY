# Calcularemos la velocidad de subida y bajada de nuestra conexión a internet. Para ello utilizaremos la librería speedtest-cli. Para instalarla ejecutamos el siguiente comando en la terminal:
# pip install speedtest-cli

# Importamos la librería
import speedtest

# Creamos el objeto
s = speedtest.Speedtest()

# Descargar la velocidad de subida
up = s.upload()

# Descargar la velocidad de bajada
down = s.download()

# Imprimir los resultados
print("La velocidad de subida es: ", up, "Mbps")
print("La velocidad de bajada es: ", down, " Mbps")
