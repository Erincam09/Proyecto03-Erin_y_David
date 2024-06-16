##################Librerias########################
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random, time
###################################################

"""
Nombre: MenuInicio
Entradas: 
Salidas: Muestra la ventana inicial del juego, se muestran los botones de iniciar y salir 
Restricciones:
"""
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
    
    """
    Nombre: salir
    Entradas:
    Salidas: Cierra el programa completamente
    Restricciones:
    """
    def salir(self):
        self.inicio.destroy()
    """
    Nombre: salirConfig
    Entradas:
    Salidas: Cierra la ventana de inicio y abre las configuraciones
    Restricciones:
    """
    def salirConfig(self):
        self.inicio.destroy()
        Config()

"""
Nombre: Config
Entradas:
Salidas: Es la ventana de configuraciones en donde se pueden elegir los distintos modos de juego
Restricciones:
"""
class Config:
    def __init__(self):
        self.menu_config = Tk()
        self.menu_config.geometry("1000x600")
        self.menu_config.title("UNO")
        self.menu_config.resizable(0, 0)

        self.imagen = Image.open("./Fondos/FondoConfig2.png")
        self.imagen = self.imagen.resize((1000, 600))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.menu_config, image=self.imagen)
        self.label_imagen.place(x=0, y=0, relheight=1, relwidth=1)
        self.imagenC1 = Image.open("./Fondos/Carta1.png")
        self.imagenC1 = self.imagenC1.resize((120, 200))
        self.imagenC1 = ImageTk.PhotoImage(self.imagenC1)
        self.solitario = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC1, command = self.iramodo1)
        self.solitario.place(x=65, y=120)

        self.imagenC2 = Image.open("./Fondos/Carta2.png")
        self.imagenC2  = self.imagenC2.resize((120, 200))
        self.imagenC2 = ImageTk.PhotoImage(self.imagenC2)
        self.jug_2 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC2, command = self.iramodo2)
        self.jug_2.place(x=250, y=120)

        self.imagenC3 = Image.open("./Fondos/Carta3.png")
        self.imagenC3  = self.imagenC3.resize((120, 200))
        self.imagenC3 = ImageTk.PhotoImage(self.imagenC3)
        self.jug_3 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC3, command = self.iramodo3)
        self.jug_3.place(x=65, y=350)

        self.imagenC4 = Image.open("./Fondos/Carta4.png")
        self.imagenC4  = self.imagenC4.resize((120, 200))
        self.imagenC4 = ImageTk.PhotoImage(self.imagenC4)
        self.jug_4 = tk.Button(self.menu_config, width=120, height=200, image=self.imagenC4, command = self.iramodo4)
        self.jug_4.place(x=250, y=350)

        self.volver= tk.Button(self.menu_config, text="Volver", bg="black", font=("Courier New", 15), fg="white", width=10, command=self.volver)
        self.volver.place(x=865, y=555)

        self.menu_config.mainloop()
    
    """
    Nombre: volver
    Entradas:
    Salidas: Se destruye la ventana de configuraciones y se abre la ventana inicial
    Restricciones:
    """
    def volver(self):
        self.menu_config.destroy()
        MenuInicio()
    def iramodo1(self):
        self.menu_config.destroy()
        OnevsCPU()
    """
    Nombre: iramodo2
    Entradas:
    Salidas: Se destruye la ventana de configuraciones y se abre la ventana de uno contra uno
    Restricciones:
    """
    def iramodo2(self):
        self.menu_config.destroy()
        OnevsOne()
    """
    Nombre: iramodo3
    Entradas:
    Salidas: Se destruye la ventana de configuraciones y se abre la ventana de juego de 3 jugadores
    Restricciones:
    """
    def iramodo3(self):
        self.menu_config.destroy()
        OnevsOnevsOne()
    """
    Nombre: iramodo4
    Entradas:
    Salidas: Se destruye la ventana de configuraciones y se abre la ventana de juego de 4 jugadores
    Restricciones:
    """
    def iramodo4(self):
        self.menu_config.destroy()
        OnevsOnevsOnevsOne()
"""
Nombre: Cartas
Entradas: color, numero
Salidas: En esta clase se crean todas las cartas segun su color o numero
Restricciones:
"""
class Cartas:
    def __init__(self,color,numero):

        self.color = color
        self.numero = numero
        self.ruta = f"./Cartas/{self.color}_{self.numero}.png"
        
        self.imagen = None
    """
    Nombre: construirimagen
    Entradas: 
    Salidas: Busca la imagen y la ajusta
    Restricciones:
    """
    def construirimagen(self):
        self.imagen = Image.open(self.ruta)
        self.imagen =  self.imagen.resize((90,150))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        return self.imagen

"""
Nombre: Mazo
Entradas:
Salidas: Manda a crear las cartas y las hace un mazo en forma de lista
Restricciones:
"""
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
    """
    Nombre: crearobjetosmazo
    Entradas:
    Salidas: crea los objetos de cartas en un mazo segun el numero,comodin y color
    Restricciones:
    """   
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
    """
    Nombre: mezclar
    Entradas:
    Salidas: mezcla el mazo de cartas 
    Restricciones:
    """ 
    def mezclar(self):
        random.shuffle(self.mazo) 
"""
Nombre: OnevsCPU
Entradas:
Salidas: Dirige a la ventana de juego de uno contra la computadora
Restricciones:
"""
class OnevsCPU:
    def __init__(self):
        self.juego1 = Tk()
        self.juego1.attributes("-fullscreen",True)
        self.juego1.title("Juego 1vCPU")
        self.imagen = Image.open("./Fondos/FondoUnoVsCPU.png")
        ancho = self.juego1.winfo_screenwidth()
        alto = self.juego1.winfo_screenheight()
        self.imagen = self.imagen.resize((ancho,alto))
        self.imagen= ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.juego1, image = self.imagen)
        self.label_imagen.place(x=0, y=0, relheight = 1, relwidth = 1)
        self.baraja = Mazo()
        self.baraja.mezclar()
        self.jugador = []
        self.computadora =[]
        self.principal = []
        self.contador = 0
        self.colorEscogido = None
    
        self.empezarjuego()
        self.juego1.mainloop()
    """
    Nombre: empezarjuego
    Entradas:
    Salidas: crea las barajas de cartas, los frames y canvas de cada jugador, inicializa el juego
    Restricciones:
    """
    def empezarjuego(self):
        for j in range(7):
            self.jugador +=[self.baraja.mazo.pop(1)]
            self.computadora +=[self.baraja.mazo.pop(1)]
        self.principal += [self.baraja.mazo.pop(1)]

        self.canvas2= tk.Canvas(self.juego1, width = 1140, height = 185, bg = "red4", scrollregion=(0, 0, 1000, 800)) 
        self.canvas2.place(x=230, y=0)
        self.canvas2.config(highlightthickness=0)

        self.canvas = tk.Canvas(self.juego1, width = 1140, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas.place(x=0, y = 570)
        self.canvas.config(highlightthickness=0)

        self.scrollbar = tk.Scrollbar(self.juego1, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.framejug = tk.Frame(self.canvas, width=700, height = 185, bg="red4") 
        self.canvas.create_window((20, 20), window=self.framejug, anchor=tk.NW)

        self.framecomp= tk.Frame(self.canvas2,bg="red4",  width=700, height = 200)
        self.canvas2.create_window((20, 20), window=self.framecomp, anchor=tk.NW)

        self.frameprin = tk.Frame(self.juego1)
        self.frameprin.place(x=560, y =310)

        self.turnojug = True
        self.comer = True
        self.coma4 = False

        self.imagenOCU2 = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU2 = self.imagenOCU2.resize((90, 150 ))
        self.imagenOCU2 = ImageTk.PhotoImage(self.imagenOCU2)
        self.botonrobar = tk.Button(self.juego1, width=90, height=150, image=self.imagenOCU2 , command = self.robarjug)
        self.botonrobar.place(x=735, y=310)

        self.imagenOCU = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU = self.imagenOCU.resize((90, 150))
        self.imagenOCU = ImageTk.PhotoImage(self.imagenOCU)

        self.mostrarcartasjugador()
        self.mostrarcartascomputadora()
        self.mostrarprincipal()
    """
    Nombre: mostrarcartasjugador
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador
    Restricciones:
    """
    def mostrarcartasjugador(self):
        for widget in self.framejug.winfo_children():
            widget.destroy() 

        for n in range(len(self.jugador)):
            carta = self.jugador[n]
            imagen = carta.construirimagen()
            self.label = tk.Label(self.framejug,image = imagen, width = 90, height = 150)
            self.label.grid(row= 0, column = n)
            self.label.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
        
        self.framejug.update_idletasks()  # Para asegurar que el framejug tiene el tamaño correcto
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    """
    Nombre: mostrarcartascomputadora
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja de la computadora
    Restricciones:
    """
    def mostrarcartascomputadora(self):

        for widget in self.framecomp.winfo_children():
            widget.destroy() 

        for n in range(len(self.computadora)):
            self.label2 = tk.Label(self.framecomp,image = self.imagenOCU, width = 90, height = 150)
            self.label2.grid(row= 0, column = n)
    """
    Nombre: mostrarprincipal
    Entradas:
    Salidas: Muestra las cartas de la baraja principal
    Restricciones:
    """
    def mostrarprincipal(self):
        for widget in self.frameprin.winfo_children():
            widget.destroy()

        ultimacarta = self.principal[-1]
        imagen = ultimacarta.construirimagen()
        self.label3 = tk.Label(self.frameprin,image = imagen, width = 90, height = 150)
        self.label3.pack()
    """
    Nombre: actualizarinterfaz
    Entradas:
    Salidas: Llama las funciones de mostrar cartas, actualizando la interfaz
    Restricciones:
    """
    def actualizarinterfaz(self):
        self.mostrarprincipal()
        self.mostrarcartasjugador()
        self.mostrarcartascomputadora()
        
    """
    Nombre: robarjug
    Entradas:
    Salidas: Permite al jugador comer cartas en caso de no tener la que se necesite
    Restricciones:
    """
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
        else:
            self.mezclarprincipal()
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
    """
    Nombre: mezclarprincipal
    Entradas:
    Salidas: Mezcla las cartas de la baraja principal y las deposita en el mazo de comer
    Restricciones:
    """
    def mezclarprincipal(self):
        if len(self.principal)>1: 
            ultimacarta = self.principal[-1]
            for elemento in self.principal:
                if elemento != ultimacarta:
                    self.baraja.mazo+=[elemento]
                    self.principal.remove(elemento)
            random.shuffle(self.baraja.mazo)
    """
    Nombre: robarcompu
    Entradas:
    Salidas: Permite a la computadora comer cartas en caso de no tener la carta necesaria
    Restricciones:
    """
    def robarcompu(self):
        if len(self.baraja.mazo) > 0:
            self.computadora+=[self.baraja.mazo.pop()]
            self.actualizarinterfaz()
            self.turnocompu()
        else:
            self.mezclarprincipal()
            self.computadora+=[self.baraja.mazo.pop()]
            self.actualizarinterfaz()
            self.turnocompu()
    """
    Nombre: validarcarta
    Entradas: carta
    Salidas: Valida si la carta presionada tiene el numero o el color con el que se debe jugar
    Restricciones:
    """
    def validarcarta(self,carta):
        ultimacarta = self.principal[-1]
        if self.turnojug == True: 
            if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                self.jugador.remove(carta)
                self.principal +=[carta]
                self.actualizarinterfaz()
                self.actualizarinterfaz()
                self.actualizarinterfaz()
                self.actualizarinterfaz()
                self.turnojug = False
                self.validarreglasticas(carta)
                self.cartaFinal()
                self.validarGane()
    """
    Nombre: validarreglasticas
    Entradas: carta
    Salidas: valida las reglas ticas, ya sea bloqueo, reversa, cambio de color, toma2 o toma4
    Restricciones:
    """
    def validarreglasticas(self, carta):
        if carta.numero == "Reversa" or carta.numero == "Bloqueo":
            if self.turnojug == False:
                self.turnojug = True
            else:
                self.turnojug = False
                self.turnocompu()
        elif carta.numero == "Toma2":
            self.contador+=2
            if self.turnojug == False:
                for elemento in self.computadora:
                    if elemento.numero == "Toma2":
                        self.computadora.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = True
                        self.validarreglasticas(elemento)
                        self.cartaFinal()
                        self.validarGane()
                        return
                self.comercarta(self.contador)
                self.contador = 0
                self.turnojug = True
            elif self.turnojug == True:
                for elemento in self.jugador:
                    if elemento.numero == "Toma2":
                        self.jugador.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = False
                        self.validarreglasticas(elemento)
                        self.cartaFinal()
                        self.validarGane()
                        return
                self.comercarta(self.contador)
                self.contador = 0
                self.turnojug = False
                self.turnocompu()
        elif carta.numero == "Toma4":
            self.contador+=4
            if self.turnojug == False:
                for elemento in self.computadora:
                    if elemento.numero == "Toma4":
                        self.computadora.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = True
                        self.validarreglasticas(elemento)
                        self.cartaFinal()
                        self.validarGane()
                        return
                self.coma4 = True
                self.comercarta(self.contador)
                self.contador = 0
                self.elegir()
                self.turnojug = True
            elif self.turnojug == True:
                for elemento in self.jugador:
                    if elemento.numero == "Toma4":
                        self.jugador.remove(elemento)
                        self.principal+=[elemento]
                        self.actualizarinterfaz()
                        self.turnojug = False
                        self.validarreglasticas(elemento)
                        self.cartaFinal()
                        self.validarGane()
                        return
                self.comercarta(self.contador)
                self.contador = 0
                for carta in self.computadora:
                    if carta.color != "Negra":
                        color =  carta.color
                        self.cambiarcolor(color)
                        messagebox.showinfo("Nuevo", f"El nuevo color es : {color}")
                        break
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
                self.actualizarinterfaz()
                print("tURNO COMP EN ESPERA")
                self.turnocompu()
    """
    Nombre: elegir
    Entradas:
    Salidas: Muestra una ventana en la que se puede elegir el color con el que se seguira jugando
    Restricciones:
    """
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
    """
    Nombre: cambiarcolor
    Entradas: colorEscogido
    Salidas: Segun el color escogido anteriormente, se cambia el atributo de color de la ultima carta en el mazo principal
    Restricciones:
    """
    def cambiarcolor(self, colorEscogido):
        if self.turnojug == False:
            self.elegirColor.destroy()
        
        ultimacarta = self.principal[-1]
        ultimacarta.color = colorEscogido

        if self.turnojug == False:
            if self.coma4 ==  False:
                self.turnocompu()
            else:
                self.turnojug = True
                self.coma4 = False
        else:
            self.turnojug = True

        return ultimacarta.color
    """
    Nombre: comercarta
    Entradas: cantidad
    Salidas: Hace que el jugador coma la cantidad de cartas ingresada
    Restricciones:
    """
    def comercarta(self, cantidad):
        if len(self.baraja.mazo) > 0:
            if self.turnojug == True:
                for x in range(cantidad):
                    self.jugador +=[self.baraja.mazo.pop()]

            else:
                for x in range(cantidad):
                    self.computadora +=[self.baraja.mazo.pop()]
        else:
            self.mezclarprincipal()
            if self.turnojug == True:
                for x in range(cantidad):
                    self.jugador +=[self.baraja.mazo.pop()]

            else:
                for x in range(cantidad):
                    self.computadora +=[self.baraja.mazo.pop()]


        self.actualizarinterfaz()
    """
    Nombre: turnocompu
    Entradas:
    Salidas: Tira una carta de la baraja de la computadora que tenga el color o el numero que se pide
    Restricciones:
    """
    def turnocompu(self):
        ultimacarta = self.principal[-1]
        if self.turnojug == False:
            for carta in self.computadora:
                if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                    self.computadora.remove(carta)
                    self.principal +=[carta]
                    self.turnojug = True
                    print("LANZADA CMP")
                    time.sleep(3)
                    self.actualizarinterfaz()
                    self.validarreglasticas(carta)
                    self.cartaFinal()
                    self.validarGane()
                    return
            
            self.robarcompu()
    """
    Nombre: cartaFinal
    Entradas:
    Salidas: Valida cuando a los jugadores les queda una carta restante
    Restricciones:
    """
    def cartaFinal(self):
        if len(self.jugador)==1:
            messagebox.showinfo("¡UNO!","Te queda una carta restante")
            return
        elif len(self.computadora)==1:
            messagebox.showinfo("¡UNO!","A tu oponente le queda una carta")
            return

    def validarGane(self):
        if self.jugador == []:
            messagebox.showinfo("Victoria","¡Felicidades, Has ganado!")
            self.juego1.destroy()
            MenuInicio()
            return
        elif self.computadora == []:
            messagebox.showinfo("Derrota","¡Has perdido!")
            self.juego1.destroy()
            MenuInicio()
            return

"""
Nombre: OnevsOne
Entradas:
Salidas: Dirige a la ventana de juego de uno contra uno
Restricciones:
"""
class OnevsOne:
    def __init__(self):
        self.juego2 = Tk()
        self.juego2.attributes("-fullscreen",True)
        self.juego2.title("Juego 1v1")
        self.imagen = Image.open("./Fondos/FondoUnoVsUno.png")
        ancho = self.juego2.winfo_screenwidth()
        alto = self.juego2.winfo_screenheight()
        self.imagen = self.imagen.resize((ancho,alto))
        self.imagen= ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.juego2, image = self.imagen)
        self.label_imagen.place(x=0, y=0, relheight = 1, relwidth = 1)
        self.baraja = Mazo()
        self.baraja.mezclar()
        self.jugador1 = []
        self.jugador2 = []
        self.principal = []
        self.contador = 0
        self.colorEscogido = None

        self.empezarjuego()
        self.juego2.mainloop()
    """
    Nombre: empezarjuego
    Entradas:
    Salidas: crea las barajas de cartas, los frames y canvas de cada jugador, inicializa el juego
    Restricciones:
    """
    def empezarjuego(self):
        for j in range(7):
            self.jugador1 +=[self.baraja.mazo.pop(1)]
            self.jugador2 +=[self.baraja.mazo.pop(1)]
        self.principal += [self.baraja.mazo.pop(1)]

        self.canvas2= tk.Canvas(self.juego2, width = 1120, height = 185, bg = "red4", scrollregion=(0, 0, 1000, 800)) 
        self.canvas2.place(x=235, y=0)
        self.canvas2.config(highlightthickness=0)

        self.canvas = tk.Canvas(self.juego2, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas.place(x=0, y = 570)
        self.canvas.config(highlightthickness=0)

        self.scrollbar = tk.Scrollbar(self.juego2, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.scrollbar2 = tk.Scrollbar(self.juego2, orient=tk.HORIZONTAL, command=self.canvas2.xview)
        self.scrollbar2.pack(side=tk.TOP, fill=tk.X)
        self.canvas2.configure(xscrollcommand=self.scrollbar2.set)

        self.framejug1 = tk.Frame(self.canvas, width=700, height = 200, bg="red4") 
        self.canvas.create_window((20, 20), window=self.framejug1, anchor=tk.NW)

        self.framejug2= tk.Frame(self.canvas2,bg="red4",  width=700, height = 200)
        self.canvas2.create_window((20, 20), window=self.framejug2, anchor=tk.NW)

        self.frameprin = tk.Frame(self.juego2)
        self.frameprin.place(x= 560, y = 310)

        self.turnojug1 = True
        self.turnojug2 = False
        self.comer = True
        self.coma4 = False
        self.comio2 = False
        self.comio4 = False

        self.imagenOCU2 = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU2 = self.imagenOCU2.resize((90, 150  ))
        self.imagenOCU2 = ImageTk.PhotoImage(self.imagenOCU2)
        self.botonrobar = tk.Button(self.juego2, width=90, height=150, image=self.imagenOCU2 , command = self.robarjug)
        self.botonrobar.place(x=735, y=310)

        self.imagenOCU = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU = self.imagenOCU.resize((90, 150))
        self.imagenOCU = ImageTk.PhotoImage(self.imagenOCU)

        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarprincipal()
    """
    Nombre: mostrarcartasjugador1
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 1
    Restricciones:
    """
    def mostrarcartasjugador1(self):
        for widget in self.framejug1.winfo_children():
            widget.destroy() 

        for n in range(len(self.jugador1)):
            carta = self.jugador1[n]
            imagen = carta.construirimagen()
            if self.turnojug1 == True:
                self.label1 = tk.Label(self.framejug1,image = imagen, width = 90, height = 150)
                self.label1.grid(row= 0, column = n)
                self.framejug1.update_idletasks()  # Para asegurar que el framejug tiene el tamaño correcto
                self.canvas.config(scrollregion=self.canvas.bbox("all"))
            else:
                self.label1 = tk.Label(self.framejug1,image =self.imagenOCU, width = 90, height = 150)
                self.label1.grid(row= 0, column = n)
            self.label1.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """"
    Nombre: mostrarcartasjugador2
    Entradas
    Salidas: Muestra las cartas que esten en la baraja del jugador 2
    Restricciones:
    """
    def mostrarcartasjugador2(self):
        for widget in self.framejug2.winfo_children():
            widget.destroy() 

        for n in range(len(self.jugador2)):
            carta = self.jugador2[n]
            imagen = carta.construirimagen()
            if self.turnojug2 == True:
                self.label2 = tk.Label(self.framejug2,image = imagen, width = 90, height = 150)
                self.label2.grid(row= 0, column = n)
                self.framejug2.update_idletasks()  # Para asegurar que el framejug tiene el tamaño correcto
                self.canvas2.config(scrollregion=self.canvas2.bbox("all"))
            else:
                self.label2 = tk.Label(self.framejug2,image = self.imagenOCU, width = 90, height = 150)
                self.label2.grid(row= 0, column = n)

            self.label2.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarprincipal
    Entradas:
    Salidas: Muestra las cartas de la baraja principal
    Restricciones:
    """
    def mostrarprincipal(self):
        for widget in self.frameprin.winfo_children():
            widget.destroy()

        ultimacarta = self.principal[-1]
        imagen = ultimacarta.construirimagen()
        self.label3 = tk.Label(self.frameprin,image = imagen, width = 90, height = 150)
        self.label3.pack()
    """
    Nombre: actualizarinterfaz
    Entradas:
    Salidas: Llama las funciones de mostrar cartas, actualizando la interfaz
    Restricciones:
    """
    def actualizarinterfaz(self):
        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarprincipal()
    """
    Nombre: robarjug
    Entradas:
    Salidas: Permite al jugador comer cartas en caso de no tener la que se necesite
    Restricciones:
    """
    def robarjug(self):
        self.comer = True
        ultimacarta = self.principal[-1]

        if self.turnojug1 == True:
            self.jugador = self.jugador1
        else:
            self.jugador = self.jugador2

        for carta in self.jugador:
            if carta.color != "Negra":
                if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero:
                    self.comer = False
                    break
        
        if len(self.baraja.mazo) > 0:
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
        else:
            self.mezclarprincipal()
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
    """
    Nombre: mezclarprincipal
    Entradas:
    Salidas: Mezcla las cartas de la baraja principal y las deposita en el mazo de comer
    Restricciones:
    """
    def mezclarprincipal(self):
        if len(self.principal)>1: 
            ultimacarta = self.principal[-1]
            for elemento in self.principal:
                if elemento != ultimacarta:
                    self.baraja.mazo+=[elemento]
                    self.principal.remove(elemento)
            random.shuffle(self.baraja.mazo)
    """
    Nombre: validarcarta
    Entradas: carta
    Salidas: Valida si la carta presionada tiene el numero o el color con el que se debe jugar
    Restricciones:
    """
    def validarcarta(self,carta):
        ultimacarta = self.principal[-1]
        if self.turnojug1 == True and self.turnojug2 == False: 
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        self.turnojug1 = False
                        self.turnojug2 = True
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        self.turnojug1 = False
                        self.turnojug2 = True
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador1.remove(carta)
                    self.principal +=[carta]
                    self.turnojug1 = False
                    self.turnojug2 = True
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()
        elif self.turnojug2 == True and self.turnojug1 == False:
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        self.turnojug2 = False
                        self.turnojug1 = True
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        self.turnojug1 = True
                        self.turnojug2 = False
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()

            else:
                if carta.numero == "Toma2":
                    self.jugador2.remove(carta)
                    self.principal +=[carta]
                    self.turnojug1 = True
                    self.turnojug2 = False
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()
    """
    Nombre: validarreglasticas
    Entradas: carta
    Salidas: valida las reglas ticas, ya sea bloqueo, reversa, cambio de color, toma2 o toma4
    Restricciones:
    """
    def validarreglasticas(self, carta):
        if carta.numero == "Reversa" or carta.numero == "Bloqueo":
            if self.turnojug2 == False:
                self.turnojug2 = True
                self.turnojug1 = False
                self.actualizarinterfaz()
            elif self.turnojug2 == True:
                self.turnojug1 = True
                self.turnojug2 = False
                self.actualizarinterfaz()
        elif carta.numero == "Toma2":
            self.contador+=2
            if self.turnojug1 == False:
                for elemento in self.jugador2:
                    if elemento.numero == "Toma2":
                        self.actualizarinterfaz()
                        self.comio2 = True
                        self.turnojug1 = False
                        self.turnojug2 = True
                        return
                self.comercarta(self.contador)
                self.comio2 = False
                self.contador = 0
                self.turnojug1 = True
                self.turnojug2 = False
            elif self.turnojug1 == True:
                for elemento in self.jugador1:
                    if elemento.numero == "Toma2":
                        self.actualizarinterfaz()
                        self.turnojug1 = True
                        self.comio2 = True
                        self.turnojug2 = False
                        return
                self.comercarta(self.contador)
                self.comio2 = False
                self.contador = 0
                self.turnojug1 = False
                self.turnojug2 = True
        elif carta.numero == "Toma4":
            self.contador+=4
            if self.turnojug1 == False:
                for elemento in self.jugador2:
                    if elemento.numero == "Toma4":
                        self.actualizarinterfaz()
                        self.turnojug1 = False
                        self.turnojug2 = True
                        self.comio4 = True
                        return
                self.coma4 = True
                self.comio4 = False
                self.comercarta(self.contador)
                self.contador = 0
                self.elegir()
                self.turnojug1 = True
                self.turnojug2 = False
            elif self.turnojug1 == True:
                for elemento in self.jugador1:
                    if elemento.numero == "Toma4":
                        self.actualizarinterfaz()
                        self.turnojug1 = True
                        self.turnojug2 = False
                        self.comio4 = True
                        return
                self.coma4 = True
                self.comercarta(self.contador)
                self.comio4 =  False
                self.contador = 0
                self.elegir()
                self.turnojug1 = False
                self.turnojug2 = True

        elif carta.numero == "CambioColor":
            if self.turnojug1 == False:
                self.elegir()
            elif self.turnojug2 == False:
                self.elegir()
    """
    Nombre: elegir
    Entradas:
    Salidas: Muestra una ventana en la que se puede elegir el color con el que se seguira jugando
    Restricciones:
    """
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
    """
    Nombre: cambiarcolor
    Entradas: colorEscogido
    Salidas: Segun el color escogido anteriormente, se cambia el atributo de color de la ultima carta en el mazo principal
    Restricciones:
    """
    def cambiarcolor(self, colorEscogido):
        self.elegirColor.destroy()
        
        ultimacarta = self.principal[-1]
        ultimacarta.color = colorEscogido

        if self.turnojug1 == False:
            if self.coma4 ==  False:
                self.turnojug2 = True
            else:
                self.turnojug1 = True
                self.turnojug2 = False
                self.coma4 = False
        
        elif self.turnojug1 == True:
            if self.coma4 ==  False:
                self.turnojug1 = True
            else:
                self.turnojug1 = False
                self.turnojug2 = True
                self.coma4 = False
        self.actualizarinterfaz()
        messagebox.showinfo("Nuevo", f"El nuevo color es : {ultimacarta.color}")
    """
    Nombre: comercarta
    Entradas: cantidad
    Salidas: Hace que el jugador coma la cantidad de cartas ingresada
    Restricciones:
    """
    def comercarta(self, cantidad):
        if len(self.baraja.mazo)==0:
            self.mezclarprincipal()

        if len(self.baraja.mazo) > 0:
            if self.turnojug1 == True:
                for x in range(cantidad):
                    self.jugador1 +=[self.baraja.mazo.pop()]

            else:
                for x in range(cantidad):
                    self.jugador2 +=[self.baraja.mazo.pop()]
    """
    Nombre: cartaFinal
    Entradas:
    Salidas: Valida cuando a los jugadores les queda una carta restante
    Restricciones:
    """
    def cartaFinal(self):
        if len(self.jugador1)==1:
            messagebox.showinfo("¡UNO!","Al jugador 1 le queda una carta restante")
            return
        elif len(self.jugador2)==1:
            messagebox.showinfo("¡UNO!","Al jugador 2 le queda una carta restante")
            return
    """
    Nombre: validarGane
    Entradas:
    Salidas: Valida cuando los jugadores ya no tienen cartas 
    Restricciones:
    """
    def validarGane(self):
        if self.jugador1 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 1, has ganado!")
            self.juego2.destroy()
            MenuInicio()
            return
        elif self.jugador2 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 2, has ganado!")
            self.juego2.destroy()
            MenuInicio()
            return
        
"""
Nombre: OnevsOnevsOne
Entradas:
Salidas: Dirige a la ventana de juego de 3 jugadores
Restricciones:
"""
class OnevsOnevsOne:
    def __init__(self):
        self.juego3 = Tk()
        self.juego3.attributes("-fullscreen",True)
        self.juego3.title("Juego 1vs1vs1")
        self.juego3.config(bg =  "red4")
        self.baraja = Mazo()
        self.baraja.mezclar()
        self.principal = []
        self.jugador1 = []
        self.jugador2 = []
        self.jugador3 = []
        
        self.contador = 0
        self.colorEscogido = None
        self.reversa = False

        self.empezarjuego()
        self.juego3.mainloop()
    """
    Nombre: empezarjuego
    Entradas:
    Salidas: crea las barajas de cartas, los frames y canvas de cada jugador, inicializa el juego
    Restricciones:
    """
    def empezarjuego(self):
        for j in range(7):
            self.jugador1 +=[self.baraja.mazo.pop(1)]
            self.jugador2 +=[self.baraja.mazo.pop(1)]
            self.jugador3 +=[self.baraja.mazo.pop(1)]

        self.principal += [self.baraja.mazo.pop(1)]

        self.canvas = tk.Canvas(self.juego3, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas.place(x=50, y = 500)
        self.canvas.config(highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.juego3, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas2 = tk.Canvas(self.juego3, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas2.place(x=50, y = 500)
        self.canvas2.config(highlightthickness=0)
        self.scrollbar2 = tk.Scrollbar(self.juego3, orient=tk.HORIZONTAL, command=self.canvas2.xview)
        self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas2.configure(xscrollcommand=self.scrollbar2.set)

        self.canvas3 = tk.Canvas(self.juego3, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas3.place(x=50, y = 500)
        self.canvas3.config(highlightthickness=0)
        self.scrollbar3 = tk.Scrollbar(self.juego3, orient=tk.HORIZONTAL, command=self.canvas3.xview)
        self.scrollbar3.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas3.configure(xscrollcommand=self.scrollbar3.set)
        
        self.framejug1 = tk.Frame(self.canvas,width=700, height = 200, bg="red4")
        self.canvas.create_window((20, 20), window=self.framejug1, anchor='nw')
        self.framejug2= tk.Frame(self.canvas2, width=700, height = 200, bg="red4")
        self.canvas2.create_window((20, 20), window=self.framejug2, anchor='nw')
        self.framejug3= tk.Frame(self.canvas3, width=700, height = 200, bg="red4")
        self.canvas3.create_window((20, 20), window=self.framejug3, anchor='nw')
        

        self.frameprin = tk.Frame(self.juego3)
        self.frameprin.place(x=515, y=290)

        self.turno = self.jugador1

        self.mostrar1 = tk.Label(self.juego3, text = "Jugador1", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar2 = tk.Label(self.juego3, text = "Jugador2", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar2.pack()
        self.mostrar3 = tk.Label(self.juego3, text = "Jugador3", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar3.pack()

        self.comer = True
        self.coma4 = False
        self.comio2 = False
        self.comio4 =  False

        self.imagenOCU2 = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU2 = self.imagenOCU2.resize((90, 150))
        self.imagenOCU2 = ImageTk.PhotoImage(self.imagenOCU2)
        self.botonrobar = tk.Button(self.juego3, width=90, height=150, image=self.imagenOCU2 , command = self.robarjug)
        self.botonrobar.place(x=740, y=290)

        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarcartasjugador3()
        self.mostrarprincipal()
    """
    Nombre: mostrarcartasjugador1
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 1
    Restricciones:
    """
    def mostrarcartasjugador1(self):
        for widget in self.framejug1.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador1:
            self.mostrar1.pack()
            self.mostrar2.pack_forget()
            self.mostrar3.pack_forget()
            self.canvas.place(x=50, y = 500)
            self.canvas2.place_forget()
            self.canvas3.place_forget()
            self.scrollbar2.pack_forget()
            self.scrollbar3.pack_forget()
            self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador1)):
                carta = self.jugador1[n]
                imagen = carta.construirimagen()
                self.label1 = tk.Label(self.framejug1,image = imagen, width = 90, height = 150)
                self.label1.grid(row= 0, column = n)
                self.label1.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarcartasjugador2
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 2
    Restricciones:
    """
    def mostrarcartasjugador2(self):
        for widget in self.framejug2.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador2:
            self.mostrar2.pack()
            self.mostrar1.pack_forget()
            self.mostrar3.pack_forget()
            self.canvas.place_forget()
            self.canvas3.place_forget()
            self.canvas2.place(x=50, y = 500)
            self.scrollbar.pack_forget()
            self.scrollbar3.pack_forget()
            self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador2)):
                carta = self.jugador2[n]
                imagen = carta.construirimagen()
                self.label2 = tk.Label(self.framejug2,image = imagen, width = 90, height = 150)
                self.label2.grid(row= 0, column = n)
                self.label2.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarcartasjugador3
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 3
    Restricciones:
    """ 
    def mostrarcartasjugador3(self):
        for widget in self.framejug3.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador3:
            self.mostrar3.pack()
            self.mostrar2.pack_forget()
            self.mostrar1.pack_forget()
            self.canvas.place_forget()
            self.canvas2.place_forget()
            self.canvas3.place(x=50, y = 500)
            self.scrollbar.pack_forget()
            self.scrollbar2.pack_forget()
            self.scrollbar3.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador3)):
                carta = self.jugador3[n]
                imagen = carta.construirimagen()
                self.label3= tk.Label(self.framejug3,image = imagen, width = 90, height = 150)
                self.label3.grid(row= 0, column = n)
                self.label3.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarprincipal
    Entradas:
    Salidas: Muestra las cartas de la baraja principal
    Restricciones:
    """
    def mostrarprincipal(self):
        for widget in self.frameprin.winfo_children():
            widget.destroy()

        ultimacarta = self.principal[-1]
        imagen = ultimacarta.construirimagen()
        self.label3 = tk.Label(self.frameprin,image = imagen, width = 90, height = 150)
        self.label3.pack()
    """
    Nombre: actualizarinterfaz
    Entradas:
    Salidas: Llama las funciones de mostrar cartas, actualizando la interfaz
    Restricciones:
    """
    def actualizarinterfaz(self):
        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarcartasjugador3()
        self.mostrarprincipal()
    """
    Nombre: robarjug
    Entradas:
    Salidas: Permite al jugador comer cartas en caso de no tener la que se necesite
    Restricciones:
    """
    def robarjug(self):
        self.comer = True
        ultimacarta = self.principal[-1]

        if self.turno == self.jugador1:
            self.jugador = self.jugador1
        if self.turno == self.jugador2:
            self.jugador = self.jugador2
        if self.turno == self.jugador3:
            self.jugador = self.jugador3

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
        else:
            self.mezclarprincipal()
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
    
    """
    Nombre: mezclarprincipal
    Entradas:
    Salidas: Mezcla las cartas de la baraja principal y las deposita en el mazo de comer
    Restricciones:
    """
    def mezclarprincipal(self):
        if len(self.principal)>1: 
            ultimacarta = self.principal[-1]
            for elemento in self.principal:
                if elemento != ultimacarta:
                    self.baraja.mazo+=[elemento]
                    self.principal.remove(elemento)
            random.shuffle(self.baraja.mazo)
    """
    Nombre: validarcarta
    Entradas: carta
    Salidas: Valida si la carta presionada tiene el numero o el color con el que se debe jugar
    Restricciones:
    """
    def validarcarta(self,carta):
        ultimacarta = self.principal[-1]
        if self.turno == self.jugador1: 
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador2
                        else:
                            self.turno = self.jugador3
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador2
                        else:
                            self.turno = self.jugador3
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador1.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador2
                    else:
                        self.turno = self.jugador3
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()

        elif self.turno == self.jugador2:
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador3 
                        else:
                            self.turno = self.jugador1
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador3 
                        else:
                            self.turno = self.jugador1
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador2.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador3 
                    else:
                        self.turno = self.jugador1
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()

        elif self.turno == self.jugador3:
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador3.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador1
                        else: 
                            self.turno = self.jugador2
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador3.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador1
                        else: 
                            self.turno = self.jugador2
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador3.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador1
                    else: 
                        self.turno = self.jugador2
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()
    """
    Nombre: validarreglasticas
    Entradas: carta
    Salidas: valida las reglas ticas, ya sea bloqueo, reversa, cambio de color, toma2 o toma4
    Restricciones:
    """
    def validarreglasticas(self, carta):
        if carta.numero == "Reversa":
            if self.reversa == False:
                self.reversa = True
                if self.turno == self.jugador2:
                    self.turno = self.jugador3 
                
                elif self.turno == self.jugador3:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador2 
            else:
                self.reversa = False
                if self.turno == self.jugador3:
                    self.turno = self.jugador2

                elif self.turno == self.jugador2:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador3

        elif carta.numero == "Bloqueo": 
            if self.reversa == False:
                if self.turno == self.jugador2:
                    self.turno = self.jugador3 
                
                elif self.turno == self.jugador3:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador2 
            else:
                if self.turno == self.jugador3:
                    self.turno = self.jugador2

                elif self.turno == self.jugador2:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador3
                
        elif carta.numero == "Toma2":
            self.contador+=2
            if self.reversa == False:
                if self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                elif self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 =  False
                    self.contador = 0
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
            else:
                if self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                elif self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
        
        elif carta.numero == "Toma4":
            self.contador+=4
            if self.reversa == False:
                if self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador2
                            self.comio4 = True
                            self.actualizarinterfaz()
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador3
                elif self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador1
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio4 =  True
                            return
                    self.coma4 = True
                    self.comio4 =  False
                    self.comercarta(self.contador)
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador2
            else:
                if self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador2
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio4 =  True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 =  False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador3
                elif self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio4 =  True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador1

        elif carta.numero == "CambioColor":
            self.elegir()
    """
    Nombre: elegir
    Entradas:
    Salidas: Muestra una ventana en la que se puede elegir el color con el que se seguira jugando
    Restricciones:
    """
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
    """
    Nombre: cambiarcolor
    Entradas: colorEscogido
    Salidas: Segun el color escogido anteriormente, se cambia el atributo de color de la ultima carta en el mazo principal
    Restricciones:
    """
    def cambiarcolor(self, colorEscogido):
        self.elegirColor.destroy()
        
        ultimacarta = self.principal[-1]
        ultimacarta.color = colorEscogido
        if self.reversa == False:
            if self.turno == self.jugador2:
                if self.coma4 ==  False:
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador3
                    self.coma4 = False
                    self.actualizarinterfaz()
            
            elif self.turno == self.jugador3:
                if self.coma4 ==  False:
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador1
                    self.coma4 = False
                    self.actualizarinterfaz()

            elif self.turno == self.jugador1:
                if self.coma4 ==  False:
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador2
                    self.coma4 = False
                    self.actualizarinterfaz()
        else:
            if self.turno == self.jugador3:
                if self.coma4 ==  False:
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador2
                    self.coma4 = False
                    self.actualizarinterfaz()
            elif self.turno == self.jugador1:
                if self.coma4 ==  False:
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador3
                    self.coma4 = False
                    self.actualizarinterfaz()
            elif self.turno == self.jugador2:
                if self.coma4 ==  False:
                   self.turno = self.jugador2
                   self.actualizarinterfaz()
                else:
                    self.turno = self.jugador1
                    self.coma4 = False
                    self.actualizarinterfaz()

        
        messagebox.showinfo("Nuevo", f"El nuevo color es : {ultimacarta.color}")
    """
    Nombre: comercarta
    Entradas: cantidad
    Salidas: Hace que el jugador coma la cantidad de cartas ingresada
    Restricciones:
    """
    def comercarta(self, cantidad):
        if len(self.baraja.mazo)==0:
            self.mezclarprincipal()

        if len(self.baraja.mazo) > 0:
            if self.turno == self.jugador1:
                for x in range(cantidad):
                    self.jugador1 +=[self.baraja.mazo.pop()]

            if self.turno == self.jugador2:
                for x in range(cantidad):
                    self.jugador2 +=[self.baraja.mazo.pop()]

            if self.turno == self.jugador3:
                for x in range(cantidad):
                    self.jugador3 +=[self.baraja.mazo.pop()]
    """
    Nombre: cartaFinal
    Entradas:
    Salidas: Valida cuando a los jugadores les queda una carta restante
    Restricciones:
    """
    def cartaFinal(self):
        if len(self.jugador1)==1:
            messagebox.showinfo("¡UNO!","Al jugador 1 le queda una carta restante")
            return
        elif len(self.jugador2)==1:
            messagebox.showinfo("¡UNO!","Al jugador 2 le queda una carta restante")
            return
        elif len(self.jugador3)==1:
            messagebox.showinfo("¡UNO!","Al jugador 3 le queda una carta restante")
            return
    """
    Nombre: validarGane
    Entradas:
    Salidas: Valida cuando los jugadores ya no tienen cartas 
    Restricciones:
    """
    def validarGane(self):
        if self.jugador1 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 1, has ganado!")
            self.juego3.destroy()
            MenuInicio()
            return
        elif self.jugador2 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 2, has ganado!")
            self.juego3.destroy()
            MenuInicio()
            return
        elif self.jugador3 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 3, has ganado!")
            self.juego3.destroy()
            MenuInicio()
            return
        
"""
Nombre: OnevsOnevsOnevsOne
Entradas:
Salidas: Dirige a la ventana de juego de 4 jugadores
Restricciones:
"""
class OnevsOnevsOnevsOne:
    def __init__(self):
        self.juego4 = Tk()
        self.juego4.attributes("-fullscreen",True)
        self.juego4.title("Juego 1vs1vs1vs1")
        self.juego4.config(bg = "red4")
        self.baraja = Mazo()
        self.baraja.mezclar()
        self.principal = []
        self.jugador1 = []
        self.jugador2 = []
        self.jugador3 = []
        self.jugador4 = []
        
        self.contador = 0
        self.colorEscogido = None
        self.reversa = False

        self.empezarjuego()
        self.juego4.mainloop()
    """
    Nombre: empezarjuego
    Entradas:
    Salidas: crea las barajas de cartas, los frames y canvas de cada jugador, inicializa el juego
    Restricciones:
    """
    def empezarjuego(self):
        for j in range(7):
            self.jugador1 +=[self.baraja.mazo.pop(1)]
            self.jugador2 +=[self.baraja.mazo.pop(1)]
            self.jugador3 +=[self.baraja.mazo.pop(1)]
            self.jugador4 +=[self.baraja.mazo.pop(1)]

        self.principal += [self.baraja.mazo.pop(1)]
        self.canvas = tk.Canvas(self.juego4, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas.place(x=50, y = 500)
        self.canvas.config(highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.juego4, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas2 = tk.Canvas(self.juego4, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas2.place(x=50, y = 500)
        self.canvas2.config(highlightthickness=0)
        self.scrollbar2 = tk.Scrollbar(self.juego4, orient=tk.HORIZONTAL, command=self.canvas2.xview)
        self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas2.configure(xscrollcommand=self.scrollbar2.set)

        self.canvas3 = tk.Canvas(self.juego4, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas3.place(x=50, y = 500)
        self.canvas3.config(highlightthickness=0)
        self.scrollbar3 = tk.Scrollbar(self.juego4, orient=tk.HORIZONTAL, command=self.canvas3.xview)
        self.scrollbar3.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas3.configure(xscrollcommand=self.scrollbar3.set)

        self.canvas4 = tk.Canvas(self.juego4, width = 1130, height = 170, bg = "red4", scrollregion=(0, 0, 1000, 800))  
        self.canvas4.place(x=50, y = 500)
        self.canvas4.config(highlightthickness=0)
        self.scrollbar4 = tk.Scrollbar(self.juego4, orient=tk.HORIZONTAL, command=self.canvas4.xview)
        self.scrollbar4.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas4.configure(xscrollcommand=self.scrollbar4.set)
        
        self.framejug1 = tk.Frame(self.canvas,width=700, height = 200, bg="red4")
        self.canvas.create_window((20, 20), window=self.framejug1, anchor='nw')
        self.framejug2= tk.Frame(self.canvas2, width=700, height = 200, bg="red4")
        self.canvas2.create_window((20, 20), window=self.framejug2, anchor='nw')
        self.framejug3= tk.Frame(self.canvas3, width=700, height = 200, bg="red4")
        self.canvas3.create_window((20, 20), window=self.framejug3, anchor='nw')
        self.framejug4= tk.Frame(self.juego4, width= 700, height = 200, bg="red4")
        self.canvas3.create_window((20, 20), window=self.framejug4, anchor='nw')

        self.frameprin = tk.Frame(self.juego4)
        self.frameprin.pack(expand = True)

        self.turno = self.jugador1

        self.mostrar1 = tk.Label(self.juego4, text = "Jugador1", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar2 = tk.Label(self.juego4, text = "Jugador2", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar2.pack()
        self.mostrar3 = tk.Label(self.juego4, text = "Jugador3", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar3.pack()
        self.mostrar4 = tk.Label(self.juego4, text = "Jugador4", bg = "red4" , fg = "black", font = ("Impact",15))
        self.mostrar4.pack()

        self.comer = True
        self.coma4 = False
        self.comio2 =  False
        self.comio4 = False

        self.imagenOCU2 = Image.open("./Cartas/Carta_Oculta.png")
        self.imagenOCU2 = self.imagenOCU2.resize((170, 270  ))
        self.imagenOCU2 = ImageTk.PhotoImage(self.imagenOCU2)
        self.botonrobar = tk.Button(self.juego4, width=170, height=270, image=self.imagenOCU2 , command = self.robarjug)
        self.botonrobar.place(x=30, y=350)

        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarcartasjugador3()
        self.mostrarcartasjugador4()
        self.mostrarprincipal()
    """
    Nombre: mostrarcartasjugador1
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 1
    Restricciones:
    """
    def mostrarcartasjugador1(self):
        for widget in self.framejug1.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador1:
            self.mostrar1.pack()
            self.mostrar2.pack_forget()
            self.mostrar3.pack_forget()
            self.mostrar4.pack_forget()
            self.canvas.place(x=50, y = 500)
            self.canvas2.place_forget()
            self.canvas3.place_forget()
            self.canvas4.place_forget()
            self.scrollbar4.pack_forget()
            self.scrollbar2.pack_forget()
            self.scrollbar3.pack_forget()
            self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador1)):
                carta = self.jugador1[n]
                imagen = carta.construirimagen()
                self.label1 = tk.Label(self.framejug1,image = imagen, width = 115, height = 180)
                self.label1.grid(row= 0, column = n)
                self.label1.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarcartasjugador2
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 2
    Restricciones:
    """
    def mostrarcartasjugador2(self):
        for widget in self.framejug2.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador2:
            self.mostrar2.pack()
            self.mostrar1.pack_forget()
            self.mostrar3.pack_forget()
            self.mostrar4.pack_forget()

            self.canvas2.place(x=50, y = 500)
            self.canvas4.place_forget()
            self.canvas.place_forget()
            self.canvas3.place_forget()
            self.scrollbar.pack_forget()
            self.scrollbar3.pack_forget()
            self.scrollbar4.pack_forget()
            self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

            for n in range(len(self.jugador2)):
                carta = self.jugador2[n]
                imagen = carta.construirimagen()
                self.label2 = tk.Label(self.framejug2,image = imagen, width = 115, height = 180)
                self.label2.grid(row= 0, column = n)
                self.label2.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarcartasjugador3
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 3
    Restricciones:
    """ 
    def mostrarcartasjugador3(self):
        for widget in self.framejug3.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador3:
            self.mostrar3.pack()
            self.mostrar2.pack_forget()
            self.mostrar1.pack_forget()
            self.mostrar4.pack_forget()
            self.canvas3.place(x=50, y = 500)
            self.canvas2.place_forget()
            self.canvas.place_forget()
            self.canvas4.place_forget()
            self.scrollbar4.place_forget()
            self.scrollbar2.pack_forget()
            self.scrollbar.pack_forget()
            self.scrollbar3.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador3)):
                carta = self.jugador3[n]
                imagen = carta.construirimagen()
                self.label3= tk.Label(self.framejug3,image = imagen, width = 115, height = 180)
                self.label3.grid(row= 0, column = n)
                self.label3.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarcartasjugador4
    Entradas:
    Salidas: Muestra las cartas que esten en la baraja del jugador 4
    Restricciones:
    """
    def mostrarcartasjugador4(self):
        for widget in self.framejug4.winfo_children():
            widget.destroy() 

        if self.turno == self.jugador4:
            self.mostrar4.pack()
            self.mostrar2.pack_forget()
            self.mostrar1.pack_forget()
            self.mostrar3.pack_forget()
            self.canvas4.place(x=50, y = 500)
            self.canvas2.place_forget()
            self.canvas3.place_forget()
            self.canvas.place_forget()
            self.canvas.pack_forget()
            self.scrollbar2.pack_forget()
            self.scrollbar3.pack_forget()
            self.scrollbar4.pack(side=tk.BOTTOM, fill=tk.X)
            for n in range(len(self.jugador4)):
                carta = self.jugador4[n]
                imagen = carta.construirimagen()
                self.label4= tk.Label(self.framejug4,image = imagen, width = 115, height = 180)
                self.label4.grid(row= 0, column = n)
                self.label4.bind("<Button-1>", lambda e, c=carta: self.validarcarta(c))
    """
    Nombre: mostrarprincipal
    Entradas:
    Salidas: Muestra las cartas de la baraja principal
    Restricciones:
    """
    def mostrarprincipal(self):
        for widget in self.frameprin.winfo_children():
            widget.destroy()

        ultimacarta = self.principal[-1]
        imagen = ultimacarta.construirimagen()
        self.label = tk.Label(self.frameprin,image = imagen, width = 115, height = 180)
        self.label.pack()
    """
    Nombre: actualizarinterfaz
    Entradas:
    Salidas: Llama las funciones de mostrar cartas, actualizando la interfaz
    Restricciones:
    """
    def actualizarinterfaz(self):
        self.mostrarcartasjugador1()
        self.mostrarcartasjugador2()
        self.mostrarcartasjugador3()
        self.mostrarcartasjugador4()
        self.mostrarprincipal()
    """
    Nombre: robarjug
    Entradas:
    Salidas: Permite al jugador comer cartas en caso de no tener la que se necesite
    Restricciones:
    """
    def robarjug(self):
        self.comer = True
        ultimacarta = self.principal[-1]

        if self.turno == self.jugador1:
            self.jugador = self.jugador1
        if self.turno == self.jugador2:
            self.jugador = self.jugador2
        if self.turno == self.jugador3:
            self.jugador = self.jugador3
        if self.turno == self.jugador4:
            self.jugador = self.jugador4

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
        else:
            self.mezclarprincipal()
            if self.comer == True:
                self.jugador+=[self.baraja.mazo.pop()]
                self.actualizarinterfaz()
            else:
                messagebox.showerror("Error","Tienes cartas disponibles para tirar")
    """
    Nombre: mezclarprincipal
    Entradas:
    Salidas: Mezcla las cartas de la baraja principal y las deposita en el mazo de comer
    Restricciones:
    """
    def mezclarprincipal(self):
        if len(self.principal)>1: 
            ultimacarta = self.principal[-1]
            for elemento in self.principal:
                if elemento != ultimacarta:
                    self.baraja.mazo+=[elemento]
                    self.principal.remove(elemento)
            random.shuffle(self.baraja.mazo)
    """
    Nombre: validarcarta
    Entradas: carta
    Salidas: Valida si la carta presionada tiene el numero o el color con el que se debe jugar
    Restricciones:
    """
    def validarcarta(self,carta):
        ultimacarta = self.principal[-1]
        if self.turno == self.jugador1: 
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador2
                        else:
                            self.turno = self.jugador4
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador1.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador2
                        else:
                            self.turno = self.jugador4
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador1.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador2
                    else:
                        self.turno = self.jugador4
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()

        elif self.turno == self.jugador2:
            if self.comio2 ==  False:
                if self.comio4 ==  False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador3 
                        else:
                            self.turno = self.jugador1
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador2.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador3 
                        else:
                            self.turno = self.jugador1
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane() 
            else:
                if carta.numero == "Toma2":
                    self.jugador2.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador3 
                    else:
                        self.turno = self.jugador1
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()
            
        elif self.turno == self.jugador3:
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador3.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador4
                        else: 
                            self.turno = self.jugador2
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador3.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador4
                        else: 
                            self.turno = self.jugador2
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador3.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador4
                    else: 
                        self.turno = self.jugador2
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()

        elif self.turno == self.jugador4:
            if self.comio2 == False:
                if self.comio4 == False:
                    if carta.color == ultimacarta.color or carta.numero == ultimacarta.numero or carta.numero == "CambioColor" or carta.numero == "Toma4":
                        self.jugador4.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador1
                        else: 
                            self.turno = self.jugador3
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
                else:
                    if carta.numero == "Toma4":
                        self.jugador4.remove(carta)
                        self.principal +=[carta]
                        if self.reversa == False:
                            self.turno = self.jugador1
                        else: 
                            self.turno = self.jugador3
                        self.validarreglasticas(carta)
                        self.actualizarinterfaz()
                        self.cartaFinal()
                        self.validarGane()
            else:
                if carta.numero == "Toma2":
                    self.jugador4.remove(carta)
                    self.principal +=[carta]
                    if self.reversa == False:
                        self.turno = self.jugador1
                    else: 
                        self.turno = self.jugador3
                    self.validarreglasticas(carta)
                    self.actualizarinterfaz()
                    self.cartaFinal()
                    self.validarGane()
                
    def validarreglasticas(self, carta):
        if carta.numero == "Reversa":
            if self.reversa == False:
                self.reversa = True
                if self.turno == self.jugador2:
                    self.turno = self.jugador4 
                
                elif self.turno == self.jugador3:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador3 

                elif self.turno == self.jugador4:
                    self.turno = self.jugador2 
            else:
                self.reversa = False
                if self.turno == self.jugador3:
                    self.turno = self.jugador1

                elif self.turno == self.jugador2:
                    self.turno = self.jugador4

                elif self.turno == self.jugador1:
                    self.turno = self.jugador3

                elif self.turno == self.jugador4:
                    self.turno = self.jugador2

        elif carta.numero == "Bloqueo": 
            if self.reversa == False:
                if self.turno == self.jugador2:
                    self.turno = self.jugador3 
                
                elif self.turno == self.jugador3:
                    self.turno = self.jugador4

                elif self.turno == self.jugador1:
                    self.turno = self.jugador2 

                elif self.turno == self.jugador4:
                    self.turno = self.jugador1
            else:
                if self.turno == self.jugador3:
                    self.turno = self.jugador2

                elif self.turno == self.jugador2:
                    self.turno = self.jugador1

                elif self.turno == self.jugador1:
                    self.turno = self.jugador4

                elif self.turno == self.jugador4:
                    self.turno = self.jugador3

        elif carta.numero == "Toma2":
            self.contador+=2
            if self.reversa == False:
                if self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                elif self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 =  False
                    self.contador = 0
                    self.turno = self.jugador4
                    self.actualizarinterfaz()
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
                elif self.turno == self.jugador4:
                    for elemento in self.jugador4:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador4
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 =  False
                    self.contador = 0
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
            else:
                if self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio2 =  True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador4
                    self.actualizarinterfaz()
                if self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 =  False
                    self.contador = 0
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                if self.turno == self.jugador4:
                    for elemento in self.jugador4:
                        if elemento.numero == "Toma2":
                            self.turno = self.jugador4
                            self.actualizarinterfaz()
                            self.comio2 = True
                            return
                    self.comercarta(self.contador)
                    self.comio2 = False
                    self.contador = 0
                    self.turno = self.jugador3
                    self.actualizarinterfaz()

        elif carta.numero == "Toma4":
            self.contador+=4
            if self.reversa == False:
                if self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio4 =  True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador3
                elif self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador4
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador2
                elif self.turno == self.jugador4:
                    for elemento in self.jugador4:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador4
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador1
            else:
                if self.turno == self.jugador3:
                    for elemento in self.jugador3:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador3
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 =  False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador2
                elif self.turno == self.jugador1:
                    for elemento in self.jugador1:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador1
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 =  False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador4
                elif self.turno == self.jugador2:
                    for elemento in self.jugador2:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador2
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador1
                elif self.turno == self.jugador4:
                    for elemento in self.jugador4:
                        if elemento.numero == "Toma4":
                            self.turno = self.jugador4
                            self.actualizarinterfaz()
                            self.comio4 = True
                            return
                    self.coma4 = True
                    self.comercarta(self.contador)
                    self.comio4 = False
                    self.contador = 0
                    self.elegir()
                    self.turno = self.jugador3

        elif carta.numero == "CambioColor":
            self.elegir()
    """
    Nombre: elegir
    Entradas:
    Salidas: Muestra una ventana en la que se puede elegir el color con el que se seguira jugando
    Restricciones:
    """
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
    """
    Nombre: cambiarcolor
    Entradas: colorEscogido
    Salidas: Segun el color escogido anteriormente, se cambia el atributo de color de la ultima carta en el mazo principal
    Restricciones:
    """
    def cambiarcolor(self, colorEscogido):
        self.elegirColor.destroy()
        
        ultimacarta = self.principal[-1]
        ultimacarta.color = colorEscogido
        if self.reversa == False:
            if self.turno == self.jugador2:
                if self.coma4 ==  False:
                    self.turno = self.jugador2
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador3
                    self.coma4 = False
                    self.actualizarinterfaz()
            
            elif self.turno == self.jugador3:
                if self.coma4 ==  False:
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador4
                    self.coma4 = False
                    self.actualizarinterfaz()

            elif self.turno == self.jugador1:
                if self.coma4 ==  False:
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador2
                    self.coma4 = False
                    self.actualizarinterfaz()

            elif self.turno == self.jugador4:
                if self.coma4 ==  False:
                    self.turno = self.jugador4
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador1
                    self.coma4 = False
                    self.actualizarinterfaz()
        else:
            if self.turno == self.jugador3:
                if self.coma4 ==  False:
                    self.turno = self.jugador3
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador2
                    self.coma4 = False
                    self.actualizarinterfaz()
            elif self.turno == self.jugador1:
                if self.coma4 ==  False:
                    self.turno = self.jugador1
                    self.actualizarinterfaz()
                else:
                    self.turno = self.jugador4
                    self.coma4 = False
                    self.actualizarinterfaz()
            elif self.turno == self.jugador2:
                if self.coma4 ==  False:
                   self.turno = self.jugador2
                   self.actualizarinterfaz()
                else:
                    self.turno = self.jugador1
                    self.coma4 = False
                    self.actualizarinterfaz()
            elif self.turno == self.jugador4:
                if self.coma4 ==  False:
                   self.turno = self.jugador4
                   self.actualizarinterfaz()
                else:
                    self.turno = self.jugador3
                    self.coma4 = False
                    self.actualizarinterfaz()

        
        messagebox.showinfo("Nuevo", f"El nuevo color es : {ultimacarta.color}")
    """
    Nombre: comercarta
    Entradas: cantidad
    Salidas: Hace que el jugador coma la cantidad de cartas ingresada
    Restricciones:
    """
    def comercarta(self, cantidad):
        if len(self.baraja.mazo)==0:
            self.mezclarprincipal()

        if len(self.baraja.mazo) > 0:
            if self.turno == self.jugador1:
                for x in range(cantidad):
                    self.jugador1 +=[self.baraja.mazo.pop()]

            elif self.turno == self.jugador2:
                for x in range(cantidad):
                    self.jugador2 +=[self.baraja.mazo.pop()]

            elif self.turno == self.jugador3:
                for x in range(cantidad):
                    self.jugador3 +=[self.baraja.mazo.pop()]

            elif self.turno == self.jugador4:
                for x in range(cantidad):
                    self.jugador4 +=[self.baraja.mazo.pop()]
    """
    Nombre: cartaFinal
    Entradas:
    Salidas: Valida cuando a los jugadores les queda una carta restante
    Restricciones:
    """
    def cartaFinal(self):
        if len(self.jugador1)==1:
            messagebox.showinfo("¡UNO!","Al jugador 1 le queda una carta restante")
            return
        elif len(self.jugador2)==1:
            messagebox.showinfo("¡UNO!","Al jugador 2 le queda una carta restante")
            return
        elif len(self.jugador3)==1:
            messagebox.showinfo("¡UNO!","Al jugador 3 le queda una carta restante")
            return
        elif len(self.jugador4)==1:
            messagebox.showinfo("¡UNO!","Al jugador 4 le queda una carta restante")
            return
    """
    Nombre: validarGane
    Entradas:
    Salidas: Valida cuando los jugadores ya no tienen cartas 
    Restricciones:
    """
    def validarGane(self):
        if self.jugador1 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 1, has ganado!")
            self.juego4.destroy()
            MenuInicio()
            return
        elif self.jugador2 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 2, has ganado!")
            self.juego4.destroy()
            MenuInicio()
            return
        elif self.jugador3 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 3, has ganado!")
            self.juego4.destroy()
            MenuInicio()
            return
        elif self.jugador4 == []:
            messagebox.showinfo("Victoria","¡Felicidades jugador 4, has ganado!")
            self.juego4.destroy()
            MenuInicio()
            return

MenuInicio()