#importamos open cv
import cv2
from cv2 import invert
from cv2 import pencilSketch
from numpy import imag

#Importamos una imagen
image = cv2.imread(r'C:\Users\Adminsena\Downloads\prubea\Popeye.png')

#La convertimos a escala de grises
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#INVERTIMOS LA IMAGEN EN ESCALA DE GRISES
inverted=255-gray_image
#Lo difuminamos
blurred=cv2.GaussianBlur(inverted,(21,21),0)

#Volvemos a invertir la imagen difuminada
invertedblur=255-blurred
#Pasamos a vosquejar
bosquejo=cv2.divide(gray_image,invertedblur,scale=256.0)

#guardamos la imagne final
cv2.imwrite('versionPopeye.png',bosquejo)