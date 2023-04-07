# Crearemos un detector de rosotros con openCV

# Importamos la librería de openCV
import numpy as np

# Instalamos la librería de openCV con pip install opencv-python
import cv2

# Importamos un algoritmo preentrenado para indentificador de cascada
cara =  cv2.CascadeClassifier('./haarcascade/haaracascade_frontalface_default.xml')

# Creamos una captura de video para la cámara web
captura = cv2.VideoCapture(0)

# Creamos un bucle infinito para que el programa no se cierre
while True:
    
    # Creamos una variable para almacenar el frame
    ret, frame = captura.read()
    
    # Creamos una variable para almacenar el frame en escala de grises
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Creamos una variable para almacenar las caras detectadas
    caras = cara.detectMultiScale(grises, 1.3, 5)
    
    # Creamos un bucle para dibujar un rectángulo alrededor de las caras
    for (x, y, w, h) in caras:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Mostramos el frame en una ventana
    cv2.imshow('frame', frame)
    
    # Creamos una condición para cerrar la ventana con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos la captura de video
captura.release()

# Cerramos todas las ventanas
cv2.destroyAllWindows()