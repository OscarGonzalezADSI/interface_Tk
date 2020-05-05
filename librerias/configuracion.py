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
import componentes as comp

def interface_fase_2(titulo, icono, color, tam_borde, estilo_borde, tipo_cursor):
    raiz = Tk()
    lbr.titulo_texto(raiz, titulo)
    lbr.titulo_icono(raiz, icono)
    lbr.color_fondo(raiz, color)
    lbr.borde_tam(raiz, tam_borde)
    lbr.borde_estilo(raiz, estilo_borde)
    lbr.cursor_tipo(raiz, tipo_cursor)
    comp.componentes(raiz)
    raiz.mainloop()

























