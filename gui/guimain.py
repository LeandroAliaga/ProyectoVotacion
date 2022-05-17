from tkinter import *
from tkinter import simpledialog

op = 'S'

def setOp(opcion, ventana):
    global op
    if opcion != 'S':
        answer = simpledialog.askstring("PASS", "ingrese contraseña de ADMIN ", parent=ventana, show="*")
        if answer == '1234':
            op = opcion
            ventana.destroy()
    else:
        op = opcion
        ventana.destroy()

def mostrarVentana():
    raiz = Tk()
    raiz.title("Sistema de Votación")
    raiz.config(bg ="navyblue")
    raiz.geometry("600x400")
    raiz.resizable (0,0)

    img = PhotoImage(file="normal.gif")
    widget = Label(raiz, image=img).grid(row=0, column=0)
    vp = Frame (raiz)

    vp = Frame (raiz)
    vp.grid (column=0, row=0, padx=(100,100), pady=(20,20))
    vp.columnconfigure (0, weight=1)
    vp.rowconfigure(0, weight=1)

    etiqueta = Label(vp, text="SISTEMA DE VOTACIÓN",
    font=("Times New Roman", 20), fg="navyblue",)
    etiqueta.grid(row=2, column=1)

    b1=Button(vp,text="Votar", font=("Times New Roman", 12), fg="black",bg ="white",
     command=lambda:setOp('V', raiz))
    b1.grid(row=3, column=1)

    b2=Button(vp,text="Escrutinio", font=("Times New Roman", 12),fg="black",bg ="white",
    command=lambda:setOp('E', raiz))
    b2.grid(row=4, column=1)

    b3=Button(vp,text="Salir", font=("Times New Roman", 12), fg="black",bg ="white",
    command=lambda:setOp('S', raiz))
    b3.grid(row=5 , column=1)

    raiz.mainloop()


def respuestaGuiMenu():
    global op
    op='S'
    mostrarVentana()
    return op
