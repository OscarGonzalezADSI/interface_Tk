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

def paquetado(marco):
    marco.pack()
