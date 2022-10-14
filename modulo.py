import hashlib
def encriptar(x):
    f = open (x)
    lineas = f.readlines ()

    h = hashlib.new ('md5')
    for linea in lineas:
        linea = str.encode (linea)

    h.update (linea)
    print ('El resultado en bits del hash es: ' + str(h.digest()))
    print ('El resultado en hexadecimales es: ' + str(h.hexdigest()))



