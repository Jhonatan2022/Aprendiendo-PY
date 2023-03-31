# pip install qrcode
# pip install image
# pip install pillow

import qrcode

# Generar el código QR
qr = qrcode.make('https://github.com/jhonatan2022')

# Crear un archivo para guardar el código QR
imgqr = open('qr.png', 'wb')

# Guardar el código QR en el archivo
qr.save(imgqr)

# Cerrar el archivo
imgqr.close()