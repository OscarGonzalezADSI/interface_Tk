from tkinter import *

def interface(titulo, icono, ancho, alto, color, redimencionamiento):
   raiz = Tk()
   titulo_texto(raiz, titulo)
   titulo_icono(raiz, icono)
   dimenciones(raiz, ancho, alto)
   color_fondo(raiz, color)
   impedir_redimencionamiento(raiz, redimencionamiento)
   raiz.mainloop()

def impedir_redimencionamiento(raiz, redimencionamiento):
    if (redimencionamiento == "horizontal"):
        raiz.resizable(True, False)
    elif(redimencionamiento == "vertical"):
        raiz.resizable(False, True)
    else:
        raiz.resizable(False, False)

def titulo_texto(raiz, titulo):
    raiz.title(titulo)

def titulo_icono(raiz, icono):
    # Tranformar imagen a (.ico)
    # https://imagen.online-convert.com/es/convertir-a-ico
    raiz.iconbitmap(icono)

def dimenciones(raiz,ancho, alto):
    dimencion = ancho +"x"+ alto
    raiz.geometry(dimencion)

def color_fondo(raiz, color):
    raiz.config(bg = color)

