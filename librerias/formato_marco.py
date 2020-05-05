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
import librerias.traduccion as trd
import librerias.marcos_proyecto as mrc

def frame_marco(modo, color_marco, ancho_marco, alto_marco, tam_borde, estilo_borde, tipo_cursor, redimencionamiento, sentido):
    sentido = trd.traduccion(redimencionamiento, sentido)
    marco = Frame()
    
    # funciones compartidas entre la raiz y los marcos (Frame) # fase 2
    lbr.color_fondo(marco, color_marco)
    lbr.borde_tam(marco, tam_borde)
    lbr.borde_estilo(marco, estilo_borde)
    lbr.cursor_tipo(marco, tipo_cursor)    
    
    # funciones exclusivas para marcos
    mrc.marco_ancho_alto(marco, ancho_marco, alto_marco)
    if (redimencionamiento == "alineacion"):
        mrc.alineacion(marco, sentido)
    elif (redimencionamiento == "expansion"):
        mrc.expansion(marco, sentido)
    elif (redimencionamiento == "orientacion"):
        mrc.orientacion(marco, sentido)
        
    return marco