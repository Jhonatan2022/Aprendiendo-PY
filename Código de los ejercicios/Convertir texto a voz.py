import pyttsx3

# Creamos el objeto
engine = pyttsx3.init()

# Definimos el texto que queremos que se convierta a voz
text = input("Escribe algo: ")

# Convertimos el texto a voz
engine.say(text)

# Ejecutamos el comando
engine.runAndWait()
