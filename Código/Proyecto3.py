import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Menu Principal
def menuInicio():
    inicio = Tk()
    inicio.geometry("1000x600")
    inicio.title("UNO")
    inicio.resizable(0,0)

    imagen = Image.open("./Fondos/Fondo2.png")
    imagen = imagen.resize((1000,600))
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(inicio, image=imagen)
    label_imagen.place(x=0, y=0, relheight=1,relwidth=1)

    def Salir():
        inicio.destroy()

    def salirConfig():
        inicio.destroy()
        config()

    salir = tk.Button(text = "Salir", bg = "black", font = ("Courier New", 15), fg = "white", width = 10, command=lambda:Salir())
    salir.place(x=5, y=555)
    iniciar = tk.Button(text = "Iniciar", bg = "black", font = ("Courier New", 15), fg = "white", width = 10, command=lambda:salirConfig())
    iniciar.place(x=865, y=555)

    inicio.mainloop()

def config():
    menu_config = Tk()
    menu_config.geometry("1000x600")
    menu_config.title("UNO")
    menu_config.resizable(0,0)

    imagen = Image.open("./Fondos/FondoConfig.png")
    imagen = imagen.resize((1000,600))
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(menu_config, image=imagen)
    label_imagen.place(x=0, y=0, relheight=1,relwidth=1)

    modo = tk.Label(text="MODO DE JUEGO:", bg = "red", font = ("Impact", 22), fg = "black")
    modo.place(x=135,y=50)

    imagenC1 = Image.open("./Fondos/Carta1.png")
    imagenC1 = imagenC1.resize((120,200))
    imagenC1 = ImageTk.PhotoImage(imagenC1)
    Solitario = tk.Button(width=120, height=200, image=imagenC1)
    Solitario.place(x=80, y=120)

    imagenC2 = Image.open("./Fondos/Carta2.png")
    imagenC2 = imagenC2.resize((120,200))
    imagenC2 = ImageTk.PhotoImage(imagenC2)
    jug_2 = tk.Button(width=120, height=200, image=imagenC2)
    jug_2.place(x=250, y=120)

    imagenC3 = Image.open("./Fondos/Carta3.png")
    imagenC3 = imagenC3.resize((120,200))
    imagenC3 = ImageTk.PhotoImage(imagenC3)
    jug_3 = tk.Button(width=120, height=200, image=imagenC3)
    jug_3.place(x=80, y=350)

    imagenC4 = Image.open("./Fondos/Carta4.png")
    imagenC4 = imagenC4.resize((120,200))
    imagenC4 = ImageTk.PhotoImage(imagenC4)
    jug_4 = tk.Button(width=120, height=200, image=imagenC4)
    jug_4.place(x=250, y=350)

    menu_config.mainloop()


menuInicio()

