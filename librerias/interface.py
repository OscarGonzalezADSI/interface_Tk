"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

from tkinter import *

    
def titulo_texto(raiz, titulo):
    raiz.title(titulo)

def titulo_icono(raiz, icono):
    raiz.iconbitmap(icono)
    # Para Tranformar cualquier imagen a (.ico)
    # https://imagen.online-convert.com/es/convertir-a-ico
    

#---------------------------------------------------------
# funciones compartidas entre la raiz y los marcos (Frame) # fase 2 (xx)
#---------------------------------------------------------
def color_fondo(raiz, color): # fase 1
    raiz.config(bg = color)

def borde_tam(raiz, tam_borde): # fase 2
    raiz.config(bd = tam_borde)
    
def borde_estilo(raiz, estilo_borde): # fase 2 (22)
    raiz.config(relief = estilo_borde)
    
def cursor_tipo(raiz, tipo_cursor): # fase 2 (23)  
    raiz.config(cursor = tipo_cursor)
    
#---------------------------------------------------------
# funciones que se mantienen por retrocompatibilidad
#---------------------------------------------------------
def interface(titulo, icono, ancho, alto, color, redimencionamiento): # fase 1 se quitaron parámetros (ancho, alto) en la fase 2
    raiz = Tk()
    titulo_texto(raiz, titulo)
    titulo_icono(raiz, icono)
    dimenciones(raiz, ancho, alto)                        # fase 1 incompatible con la fase 2 
    color_fondo(raiz, color)                              # fase 1 funcion compartida entre la raiz y los marcos (Frame) # fase 2
    impedir_redimencionamiento(raiz, redimencionamiento)  # fase 1 incompatible con la fase 2
    raiz.mainloop()

def dimenciones(raiz,ancho, alto): # fase 1 incompatible con la fase 2
    dimencion = ancho +"x"+ alto
    raiz.geometry(dimencion)

def impedir_redimencionamiento(raiz, redimencionamiento): # fase 1 incompatible con la fase 2
    if (redimencionamiento == "horizontal"):
        raiz.resizable(True, False)
    elif(redimencionamiento == "vertical"):
        raiz.resizable(False, True)
    else:
        raiz.resizable(False, False)







