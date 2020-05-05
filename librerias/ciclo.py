"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

import librerias.EtiquetasTexto as lbtex

def ciclo(miframe, modo, texto, espaciado, interlineado):  
    y = 0
    while(len(texto)>y):
        milabel_x = 0
        milabel_y = interlineado*y
        
        x = 0
        i = 1
        while(len(texto[y])>x):
            leyenda = texto[y][x][0]
            color = texto[y][x][1]
            tam = texto[y][x][3]
            tipo_letra = texto[y][x][2]
            lbtex.etiquetas_modo(miframe, modo,  milabel_x, milabel_y, leyenda, color, tam, tipo_letra)
            milabel_x += espaciado*i
            x+=1

        y += 1











