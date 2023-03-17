from PIL import Image

#Abrimos la imagen original 
imagen = Image.open(r'C:\Users\JHONATAN FLOREZ\Documents\PYTHON\Implementando opencv\evidencia\popeye.png')

print("Size: ",imagen.size)

#Redimensionamos la imagen con la cantidad de "pixeles"
imagenSmall = imagen.resize((32,32),resample=Image.BILINEAR)

#Reescalamos a la imagen original pero implementando la difuminacion
difumino = imagenSmall.resize(imagen.size,Image.NEAREST)

#Guardamos el resultado con el nombre que queramos
print('Baneado por ser demaciado sensual', difumino.save('nuevo.png'))