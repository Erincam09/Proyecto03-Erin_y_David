import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
        
        self.imagen = None

    def construirimagen(self):
        self.imagen = Image.open(self.ruta)
        self.imagen = ImageTk.PhotoImage(self.imagen)
        return self.imagen
class Mazo:
    def __init__(self):
        self.mazo = []
        self.listacolores = ["Roja","Azul","Verde","Amarilla"]
        self.listanumeros = [0,1,2,3,4,5,6,7,8,9]
        self.listacomodines = ["Toma2","Reversa","Bloqueo"]

        self.listanumeros2 = [1,2,3,4,5,6,7,8,9]
        self.colorextra = ["Negra", "Negra","Negra", "Negra"]
        self.cartaextra = ["Toma4","CambioColor"]

        self.crearobjetosmazo()
        
    def crearobjetosmazo (self):
        
        for color in self.listacolores:
            for numero in self.listanumeros:
                carta = Cartas(color,numero)
                self.mazo+=[carta]
            for comodin in self.listacomodines:
                carta = Cartas(color,comodin)
                self.mazo+=[carta]

        for color in self.listacolores:
            for numero in self.listanumeros2:
                carta = Cartas(color,numero)
                self.mazo+=[carta]
            for comodin in self.listacomodines:
                carta = Cartas(color,comodin)
                self.mazo+=[carta]

        for color in self.colorextra:
            for extra in self.cartaextra:
                carta = Cartas(color,extra)
                self.mazo+=[carta]

    def mezclar(self):
        random.shuffle(self.mazo) 
class OnevsOne:
    def __init__(self):
        self.juego1 = Tk()
        self.juego1.attributes("-fullscreen",True)
        self.juego1.title("Juego 1v1")
        self.juego1.config(bg =  "red4")
        self.baraja = Mazo()
        self.baraja.mezclar()
        self.jugador = []
        self.computadora =[]
        self.principal = []
        self.contador = 0
        self.colorEscogido = None
    
        self.empezarjuego()
        self.juego1.mainloop()
    def empezarjuego(self):
        for j in range(7):
            self.jugador +=[self.baraja.mazo.pop(1)]
            self.computadora +=[self.baraja.mazo.pop(1)]
        self.principal += [self.baraja.mazo.pop(1)]

        self.framejug = tk.Frame(self.juego1, width= 1000,bg="red4")
        self.framejug.pack(side='bottom', pady=10, padx = 10)

        self.framecomp= tk.Frame(self.juego1,bg="red4")
        self.framecomp.pack()

        self.frameprin = tk.Frame(self.juego1)
        self.frameprin.pack(expand = True)

        self.turnojug = True
        self.comer = True

        self.imagenOCU2 = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU2 = self.imagenOCU2.resize((170, 270  ))
        self.imagenOCU2 = ImageTk.PhotoImage(self.imagenOCU2)
        self.botonrobar = tk.Button(self.juego1, width=170, height=270, image=self.imagenOCU2 , command = self.robarjug)
        self.botonrobar.place(x=30, y=350)

        self.imagenOCU = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU = self.imagenOCU.resize((115, 180))
        self.imagenOCU = ImageTk.PhotoImage(self.imagenOCU)


        self.mostrarcartasjugador()
        self.mostrarcartascomputadora()
        self.mostrarprincipal()

    def mostrarcartasjugador(self):
        for widget in self.framejug.winfo_children():
            widget.destroy() 

        for n in range(len(self.jugador)):
            carta = self.jugador[n]
            imagen = carta.construirimagen()
            self.label = tk.Label(self.framejug,image = imagen, width = 115, height = 180)
            self.label.grid(row= 0, column = n)
            self.label.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))

    def mostrarcartascomputadora(self):

        for widget in self.framecomp.winfo_children():
            widget.destroy() 

        for n in range(len(self.computadora)):
            carta = self.computadora[n]
            imagen = carta.construirimagen()
            self.label2 = tk.Label(self.framecomp,image = imagen, width = 115, height = 180)
            self.label2.grid(row= 0, column = n)

    def mostrarprincipal(self):
        for widget in self.frameprin.winfo_children():
            widget.destroy()

        ultimacarta = self.principal[-1]
        imagen = ultimacarta.construirimagen()
        self.label3 = tk.Label(self.frameprin,image = imagen, width = 115, height = 180)
        self.label3.pack()

    def actualizarinterfaz(self):
        self.mostrarcartasjugador()
        self.mostrarcartascomputadora()
        self.mostrarprincipal()
    
    def robarjug(self):
        self.comer = True
        ultimacarta = self.principal[-1]

        for carta in self.jugador:
            if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero:
                self.comer = False
                break
        

        if len(self.baraja.mazo) > 0:
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
                  
    def robarcompu(self):
        if len(self.baraja.mazo) > 0:
            self.computadora+=[self.baraja.mazo.pop()]
            self.actualizarinterfaz()
            self.turnocompu()

    def validarcarta(self,carta):
        ultimacarta = self.principal[-1]
        if self.turnojug == True: 
            if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor":
                self.jugador.remove(carta)
                self.principal +=[carta]
                self.turnojug = False
                self.actualizarinterfaz()
                self.validarreglasticas(carta)
                self.cartaFinal()
                self.validarGane()

    def validarreglasticas(self, carta):
        if carta.numero == "Reversa" or carta.numero == "Bloqueo":
            if self.turnojug == False:
                self.turnojug = True
            else:
                self.turnojug = False
                self.turnocompu()
        elif carta.numero == "Toma2":
            if self.turnojug == False:
                for elemento in self.computadora:
                    if elemento.numero == "Toma2":
                        self.contador +=2
                        self.computadora.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = True
                        self.validarreglasticas(elemento)
                        return
                self.comercarta(self.contador)
                self.contador = 0
                self.turnojug = True
            else:
                for elemento in self.jugador:
                    if elemento.numero == "Toma2":
                        self.jugador.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = False
                        self.validarreglasticas(elemento)
                        return
                self.comercarta(self.contador)
                self.contador = 0
                self.turnojug = False
                self.turnocompu()
        elif carta.numero == "CambioColor":
            if self.turnojug == False:
                self.elegir()
            elif self.turnojug == True:
                for carta in self.computadora:
                    if carta.color != "Negra":
                        color =  carta.color
                        self.cambiarcolor(color)
                        messagebox.showinfo("Nuevo", f"El nuevo color es : {color}")
                        return
        else:
            if self.turnojug == False:
                self.turnocompu()
                
    def elegir(self):
        self.elegirColor = Toplevel()
        self.elegirColor.geometry("700x400")
        self.elegirColor.resizable(0,0)
        self.elegirColor.title("Cambio Color")
        self.elegirColor.config(bg="black")

        self.opciones = tk.Label(self.elegirColor, text="Elija un color:", bg="black", font=("Impact", 22), fg="red4")
        self.opciones.place(x=265,y=35)

        self.cartaRoja = Image.open("./Cartas/Carta_Roja.png")
        self.cartaRoja = self.cartaRoja.resize((120, 200))
        self.cartaRoja = ImageTk.PhotoImage(self.cartaRoja)

        self.cartaAzul = Image.open("./Cartas/Carta_Azul.png")
        self.cartaAzul  = self.cartaAzul.resize((120, 200))
        self.cartaAzul = ImageTk.PhotoImage(self.cartaAzul)

        self.cartaAmarilla = Image.open("./Cartas/Carta_Amarilla.png")
        self.cartaAmarilla  = self.cartaAmarilla.resize((120, 200))
        self.cartaAmarilla = ImageTk.PhotoImage(self.cartaAmarilla)

        self.cartaVerde = Image.open("./Cartas/Carta_Verde.png")
        self.cartaVerde  = self.cartaVerde.resize((120, 200))
        self.cartaVerde = ImageTk.PhotoImage(self.cartaVerde)


        self.colorRojo = tk.Button(self.elegirColor, width=120, height=200, image=self.cartaRoja, command=lambda:self.cambiarcolor("Roja"))
        self.colorRojo.place(x=50, y=120)

        self.colorAzul = tk.Button(self.elegirColor, width=120, height=200, image=self.cartaAzul, command=lambda:self.cambiarcolor("Azul"))
        self.colorAzul.place(x=210, y=120)

        self.colorAmarillo = tk.Button(self.elegirColor, width=120, height=200, image=self.cartaAmarilla, command=lambda:self.cambiarcolor("Amarilla"))
        self.colorAmarillo.place(x=370, y=120)

        self.colorVerde = tk.Button(self.elegirColor, width=120, height=200, image=self.cartaVerde, command=lambda:self.cambiarcolor("Verde"))
        self.colorVerde.place(x=530, y=120)

        self.elegirColor.mainloop()
    
    def cambiarcolor(self, colorEscogido):
        if self.turnojug == False:
            self.elegirColor.destroy()
        
        ultimacarta = self.principal[-1]
        ultimacarta.color = colorEscogido

        if self.turnojug == False:
            self.turnocompu()
        else:
            self.turnojug = True

        return ultimacarta.color
       
    
    def comercarta(self, cantidad):
        if self.turnojug == True:
            for x in range(cantidad):
                self.jugador +=[self.baraja.mazo.pop()]

        else:
            for x in range(cantidad):
                self.computadora +=[self.baraja.mazo.pop()]

        self.actualizarinterfaz()

    def turnocompu(self):
        ultimacarta = self.principal[-1]
        for carta in self.computadora:
            if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor":
                self.computadora.remove(carta)
                self.principal +=[carta]
                self.turnojug = True
                self.actualizarinterfaz()
                self.validarreglasticas(carta)
                return
            
        self.robarcompu()

    def cartaFinal(self):
        if len(self.jugador)==1:
            messagebox.showinfo("¡UNO!","Te queda una carta restante")
        elif len(self.computadora)==1:
            messagebox.showinfo("¡UNO!","A tu oponente le queda una carta")

    def validarGane(self):
        if self.jugador == []:
            messagebox.showinfo("Victoria","¡Felicidades, Has ganado!")
            self.juego1.destroy()
            MenuInicio()
        elif self.computadora == []:
            messagebox.showinfo("Derrota","¡Has perdido!")
            self.juego1.destroy()
            MenuInicio()
        
    


        
MenuInicio()