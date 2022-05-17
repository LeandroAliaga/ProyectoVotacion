from tkinter import *

op = ''

def setOp(contrasenia, ventana):
    global op
    op = contrasenia
    ventana.destroy()

def mostrarVentana():
    raiz = Tk()
    raiz.title("Autenticación")
    raiz.config(bg = "navyblue")
    raiz.geometry("600x400")
    raiz.resizable (0,0)

    img = PhotoImage(file="normal.gif")
    widget = Label(raiz, image=img).grid(row=0, column=0)
    vp = Frame (raiz)


    vp.grid (column=0, row=0, padx=(100,100), pady=(20,20))
    vp.columnconfigure (0, weight=1)
    vp.rowconfigure(0, weight=1)


    etiqueta = Label(vp, text="AUTENTICACIÓN",
    font=("Times New Roman", 20), fg="navyblue",)
    etiqueta.grid(row=1, column=0)

    etiqueta = Label(vp, text="Ingrese la contraseña del Administrador",
    font=("Times New Roman", 12),fg="navyblue",)
    etiqueta.grid(row=2, column=0)


    mitexto=StringVar()
    textoentry=StringVar()
    entry1=Entry(vp ,textvar=textoentry, show= "*" ).grid()

    #label1=Label(vp ,textvar=mitexto,).grid()

    b1=Button(vp ,text="AUTENTICAR",fg="navyblue",bg ="white",
     command=lambda:setOp(textoentry.get(), raiz)).grid()

    raiz.mainloop()


def respuestaGuiAuth():
    mostrarVentana()
    return op
