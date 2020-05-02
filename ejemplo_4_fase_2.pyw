"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

from tkinter import *

import librerias.interface as lbr
import librerias.marcos as mrc

def configuracion_raiz():
    titulo = "ventana con redimencionamiento vertical"
    icono = "imagenes/imagen.ico"
    color = "blue"
    tam_borde = "10"
    estilo_borde = "sunken"
    tipo_cursor = "arrow"
    interface_fase_2(titulo, icono, color, tam_borde, estilo_borde, tipo_cursor)

def interface_fase_2(titulo, icono, color, tam_borde, estilo_borde, tipo_cursor):
    raiz = Tk()
    lbr.titulo_texto(raiz, titulo)
    lbr.titulo_icono(raiz, icono)
    lbr.color_fondo(raiz, color)
    lbr.borde_tam(raiz, tam_borde)
    lbr.borde_estilo(raiz, estilo_borde)
    lbr.cursor_tipo(raiz, tipo_cursor)
    equipo_marcos()
    raiz.mainloop()

def configuracion_marco():
    color_marco = "red"
    ancho_marco = "600"
    alto_marco = "100"
    tam_borde = "10"
    estilo_borde = "sunken"
    tipo_cursor = "arrow"
    redimencionamiento = "expansion" #(21)
    sentido = "horizontal" #(21)
    mrc.marco(color_marco, ancho_marco, alto_marco, tam_borde, estilo_borde, tipo_cursor, redimencionamiento, sentido)
    
def equipo_marcos():
    configuracion_marco()

configuracion_raiz()
""" 
    # ------------------------------------------------------
      (21) redimencionamiento   sentido 
    # ------------------------------------------------------
        "expansion"             "horizontal"
                                "vertical"
                                "ambos"
                             
        "alineacion"            "izquierda", "left"
                                "derecha",   "right"
                                "arriba",    "top"
                                "abajo",     "bottom"
                             
        "orientacion"           "norte"
                                "noreste"
                                "este"
                                "sureste"
                                "sur"
                                "suroeste"
                                "oeste"
                                "noroeste"
                                "centrado"
    # ------------------------------------------------------
      (22) tipos de borde:
    # ------------------------------------------------------
        "raised"   "sunken"   "flat"   "groove"   "ridge"
        
        fuente: 
        https://docs.python.org/3/library/tkinter.html#tk-option-data-types
        
    # ------------------------------------------------------                       
      (23) tipos de cursor:
    # ------------------------------------------------------
        "arrow"      "circle"   "clock"     "cross"    "dotbox"
        "exchange"   "fleur"    "heart"     "man"      "mouse"
        "pirate"     "plus"     "shuttle"   "sizing"   "spider"
        "spraycan"   "star"     "target"    "tcross"   "trek"
        "watch"
        
        fuente:
        https://www.tutorialspoint.com/python/tk_cursors.htm
"""
