import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

class MenuInicio:
    def __init__(self):
        self.inicio = Tk()
        self.inicio.geometry("1000x600")
        self.inicio.title("UNO")
        self.inicio.resizable(0, 0)

        self.imagen = Image.open("./Fondos/Fondo2.png")
        self.imagen = self.imagen.resize((1000, 600))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.inicio, image=self.imagen)
        self.label_imagen.place(x=0, y=0, relheight=1, relwidth=1)

        self.salir = tk.Button(self.inicio, text="Salir", bg="black", font=("Courier New", 15), fg="white", width=10, command=self.salir)
        self.salir.place(x=5, y=555)
        self.iniciar = tk.Button(self.inicio, text="Iniciar", bg="black", font=("Courier New", 15), fg="white", width=10, command=self.salirConfig)
        self.iniciar.place(x=865, y=555)

        self.inicio.mainloop()

    def salir(self):
        self.inicio.destroy()

    def salirConfig(self):
        self.inicio.destroy()
        Config()

class Config:
    def __init__(self):
        self.menu_config = Tk()
        self.menu_config.geometry("1000x600")
        self.menu_config.title("UNO")
        self.menu_config.resizable(0, 0)

        self.imagen = Image.open("./Fondos/FondoConfig.png")
        self.imagen = self.imagen.resize((1000, 600))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.menu_config, image=self.imagen)
        self.label_imagen.place(x=0, y=0, relheight=1, relwidth=1)

        self.modo = tk.Label(self.menu_config, text="MODO DE JUEGO:", bg="red", font=("Impact", 22), fg="black")
        self.modo.place(x=135, y=50)

        self.imagenC1 = Image.open("./Fondos/Carta1.png")
        self.imagenC1 = self.imagenC1.resize((120, 200))
        self.imagenC1 = ImageTk.PhotoImage(self.imagenC1)
        self.solitario = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC1, command = self.iramodo1)
        self.solitario.place(x=80, y=120)

        self.imagenC2 = Image.open("./Fondos/Carta2.png")
        self.imagenC2  = self.imagenC2.resize((120, 200))
        self.imagenC2 = ImageTk.PhotoImage(self.imagenC2)
        self.jug_2 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC2)
        self.jug_2.place(x=250, y=120)

        self.imagenC3 = Image.open("./Fondos/Carta3.png")
        self.imagenC3  = self.imagenC3.resize((120, 200))
        self.imagenC3 = ImageTk.PhotoImage(self.imagenC3)
        self.jug_3 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC3)
        self.jug_3.place(x=80, y=350)

        self.imagenC4 = Image.open("./Fondos/Carta4.png")
        self.imagenC4  = self.imagenC4.resize((120, 200))
        self.imagenC4 = ImageTk.PhotoImage(self.imagenC4)
        self.jug_4 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC4)
        self.jug_4.place(x=250, y=350)

        self.menu_config.mainloop()
    
    def iramodo1(self):
        self.menu_config.destroy()
        OnevsOne()

class Cartas:
    def __init__(self,color,numero):

        self.color = color
        self.numero = numero
        self.ruta = f"./Cartas/{self.color}_{self.numero}.png"
        print(self.ruta)
        self.imagen = None

    def construirimagen(self):
        self.imagen = Image.open(self.ruta)
        self.imagen = ImageTk.PhotoImage(self.imagen)

class Mazo:
    def __init__(self):
        self.mazo = []
        self.listacolores = ["Rojo","Azul","Verde","Amarilla"]
        self.listanumeros = [0,1,2,3,4,5,6,7,8,9]
        self.listacomodines = ["Toma2","Reversa","Bloqueo"]

        self.crearobjetosmazo()
        
    def crearobjetosmazo (self):
        
        for color in self.listacolores:
            for numero in self.listanumeros:
                carta = Cartas(color,numero)
                self.mazo+=[carta]
            for comodin in self.listacomodines:
                carta = Cartas(color,comodin)
                self.mazo+=[carta]

    def mezclar(self):
        random.shuffle(self.mazo)

      
class OnevsOne:
    def __init__(self):
        self.juego1 = Tk()
        self.juego1.attributes("-fullscreen",True)
        self.juego1.title("Juego 1v1")
        self.baraja = Mazo()
        self.baraja.mezclar()
        
        
        

        






MenuInicio()