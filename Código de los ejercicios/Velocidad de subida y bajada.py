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
