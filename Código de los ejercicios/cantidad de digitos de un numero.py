# Mostraremos las dos formas de hacerlos

# Forma 1
n1= 500

# Convertimos el numero a string y luego contamos la cantidad de caracteres
digitos = len(str(n1))

# Mostramos la cantidad de digitos
print(digitos)

#---------------------------------------------------------------------------------------------
# Forma 2
n2 = 5000
digitos2 = 0

# Mientras el numero sea mayor a 0
while n2 > 0:

    # Dividimos el numero entre 10 y lo redondeamos hacia abajo
    n2 = n2 // 10

    # Incrementamos la cantidad de digitos en 1 
    # También podemos incrementar el numero digitos2 = digitos2 + 1
    digitos2 += 1 

# Mostramos la cantidad de digitos
print(digitos2)