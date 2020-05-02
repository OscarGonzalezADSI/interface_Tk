"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

#---------------------------------------------------------
# sistema de traducción de parámetros de usabilidad       # fase 2
#---------------------------------------------------------
def traduccion(redimencionamiento, sentido):
    if (redimencionamiento == "alineacion"):
        sentido = traduccion_alineacion(sentido)
    elif (redimencionamiento == "expansion"):
        sentido = traduccion_expansion(sentido)
    elif (redimencionamiento == "orientacion"):
        sentido = traduccion_orientacion(sentido)
    else:
        sentido =""
    return sentido

def traduccion_alineacion(sentido):
    if(sentido == "izquierda" or sentido == "left"):
        sentido = "left"
    elif(sentido == "derecha" or sentido == "right"):
        sentido = "right"
    elif(sentido == "arriba" or sentido == "top"):
        sentido = "top"
    elif(sentido == "abajo" or sentido == "bottom"):
        sentido = "bottom"
    else:
        sentido = ""
    return sentido

def traduccion_expansion(sentido):
    if(sentido == "horizontal"):
        sentido = "x"
    elif(sentido == "vertical"):
        sentido = "y"
    elif(sentido == "ambos"):
        sentido = "both"
    else:
        sentido = ""
    return sentido

def traduccion_orientacion(sentido):
    if(sentido == "norte"):
        direccion = ("top", "n")
    elif(sentido == "noreste"):
        direccion = ("right", "ne")
    elif(sentido == "este"):
        direccion = ("right", "e")
    elif(sentido == "sureste"):
        direccion = ("right", "se")
    elif(sentido == "sur"):
        direccion = ("bottom", "s")
    elif(sentido == "suroeste"):
        direccion = ("left", "sw")
    elif(sentido == "oeste"):
        direccion = ("left", "w")
    elif(sentido == "noroeste"):
        direccion = ("left", "nw")
    elif(sentido == "centrado"):
        direccion = ("bottom", "center")
    else:
        sentido = ""
    return direccion
