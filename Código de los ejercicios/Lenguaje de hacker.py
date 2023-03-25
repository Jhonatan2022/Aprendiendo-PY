# Creamos un diccionario con las letras y números que queremos convertir
diccionario = {
    "A":"4",
    "B":"I3",
    "C":"[",
    "D":")",
    "E":"3",
    "F":"|=",
    "G":"&",
    "H":"#",
    "I":"1",
    "J":",_|",
    "K":">|",
    "L":"1",
    "M":"JVI",
    "N":"^/",
    "O":"0",
    "P":"|*",
    "Q":"(_,)",
    "R":"I2",
    "S":"5",
    "T":"7",
    "U":"(_)",
    "V":"|/",
    "W":"\/\/",
    "X":"><",
    "Y":"j",
    "Z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o",
}

# Creamos una función que reciba un texto y lo convierta
def conversor (texto):

    texto_convertido = "La traducción del texto es: "

    # Creamos un bucle que recorra el texto y lo convierta
    for i in range(len(texto)):
        # Pasamos la letra a mayúsculas para que no haya problemas con las minúsculas
        letra = texto.upper()[i]

        # Si la letra está en el diccionario, la sustituimos por su valor y la añadimos al texto convertido
        if letra in diccionario:

            # Si la letra es una "I" y la letra anterior es un espacio, la sustituimos por un "1"
            texto_convertido += diccionario[letra]
        else:
            texto_convertido += letra
    return texto_convertido

texto = input("Introduce el texto que quieras traducir: ")
print(conversor(texto))