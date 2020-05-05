"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

from tkinter import *

def ubicacion_general(milabel):
    milabel_x = 100
    milabel_y = 100
    milabel.place(x=milabel_x, y=milabel_y)
    
# -----------------------------------------------------
# Métodos de texto
# -----------------------------------------------------
def etiquetas_modo(miframe, modo, milabel_x, milabel_y, texto, color, tam, tipo_letra):
    if(modo == "paquete"):
        etiquetas_paquetadas(miframe, texto)
    elif(modo == "ubicacion"):
        ubicacion(miframe, milabel_x, milabel_y, texto)
    elif(modo == "formato"):
        formato(miframe, milabel_x, milabel_y, texto, color, tam, tipo_letra)
        
def etiquetas_paquetadas(miframe, texto):
    milabel = Label(miframe, text=texto)
    paquetado(milabel)

def paquetado(marco):
    marco.pack()

def ubicacion(miframe, milabel_x, milabel_y, texto):
    Label(miframe, text=texto).place(x=milabel_x, y=milabel_y)

def formato(miframe, milabel_x, milabel_y, texto, color, tam, tipo_letra):
    Label(miframe, text=texto, fg = color, font=(tipo_letra, tam)).place(x=milabel_x, y=milabel_y)




# -------------------------------------------------------
# miImagen = PhotoImage(file="../imagenes/Captura.PNG")
# Label(miframe, image=miImagen).place(x = 100, y = 100)
"""
# -------------------------------------------------------
from tkinter import *
root = Tk()

miframe = Frame(root, width = 500, height = 400)
miframe.pack()

miImagen = PhotoImage(file="../imagenes/Captura.PNG")
Label(miframe, image=miImagen).place(x = 100, y = 100)

# texto
# ----------------------------------------------------
# milabel = Label(miframe, text="hola")
# milabel.pack()
# milabel.place(x = 100, y = 100)
# Label(miframe, text="hola").place(x = 100, y = 100)
# Label(miframe, text="hola", fg = "red", font=(18)).place(x = 100, y = 100)
Label(miframe, text="hola", fg = "red", font=("Comic Sans MS", 18)).place(x = 200, y = 200)

root.mainloop()
# -------------------------------------------------------
"""



















"""

text
anchor
BG
bitmap
Bd
Font
Fg
Width
Height
Image
Justify

"""