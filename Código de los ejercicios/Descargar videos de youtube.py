# Crearemos un herramienta para descargar videos de youtube

# Importamos la librería de youtube_dl
from pytube import YouTube

# Importamos la librería de os para poder crear carpetas
import os

# Importamos la librería de tkinter para crear la interfaz gráfica
from tkinter import *

# Importamos messagebox para mostrar mensajes de error
from tkinter import messagebox as MessageBox

# Creamos la ventana
ventana = Tk()
# Configuramos la ventana
ventana.config(bd=15)

# Definimos el título de la ventana
ventana.title("Descargar videos de youtube")


def accion():

    # Creamos la variable para almacenar la url del video
    enlace =video.get()
    video = YouTube(enlace)


instrucciones = Label(ventana, text="Ingresa la url del video que deseas descargar")
instrucciones.grid(row=0, column=1)

# Creamos la variable para almacenar la url del video
video = Entry(ventana)
video.grid(row=0, column=1)

# Creamos el botón para descargar el video
boton = Button(ventana, text="Descargar", command = accion)