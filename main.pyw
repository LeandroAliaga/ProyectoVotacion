from funciones import *
from gui.guimain import *
from gui.guiautenticacion import *
from gui.guivotar import *
from gui.guiescrutinio import *

PASS = "1234"

userpass = respuestaGuiAuth()

if (userpass == PASS):

    op= " "
    while op.upper() != 'S':

        op= respuestaGuiMenu()

        if op.upper() == 'V':
            op= respuestaGuiVotar()

        if op.upper() == "E":
            op= respuestaGuiEscrutinio()

    input('Gracias! vuelva prontoss')

else:
    input('lo que ustedes quieran!!')
