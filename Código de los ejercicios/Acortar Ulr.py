# pip install pyshorteners

import pyshorteners

# URL a acortar
url = 'https://github.com/jhonatan2022'

# Crear el objeto
s = pyshorteners.Shortener()

# Acoratar la URL
short = s.tinyurl.short(url)

# Acortar la URL
print('La url acortada es: ', short)