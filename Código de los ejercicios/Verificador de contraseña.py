contraseña = False

# Pedimos la contraseña

for i in input("Introduzca su contraseña que contenga al menos @ * #: "):
    # Comprobamos que la contraseña tenga al menos 8 caracteres, una mayúscula y un número
    if i == ("@" and "*" and "#"):
        contraseña = True

if contraseña == True:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")
