import hashlib

from modulo import encriptar

# El usuario ingresa la la dirección del archivo que va a utilizar
x= str (input("Dijite la dirección de su archivo: "))

encriptar(x)


from escrita import encriptar

# El usuario ingresa la contraseña que va a utilizar
contraseña = input("Contraseña: ")

encriptar(contraseña)