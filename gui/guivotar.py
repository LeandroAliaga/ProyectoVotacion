from tkinter import *
from tkinter import messagebox
import pymysql

def registrarVoto(voto, ventana):
    listas = ('Lista 1', 'Lista 2', 'Lista 3', ' en blanco')

    answer = messagebox.askyesno("Confirmacion","desea votar " + listas[voto-1] + " ?")
    if answer:
        conect = pymysql.connect(host="localhost",user="root",passwd="12345",db="votacion")
        cursor = conect.cursor()
        cursor.execute(
            "INSERT INTO votos (idlista,fecha) VALUES (%s, null)",
            (voto)
        )
        conect.commit()
        cursor.close()
        conect.close()
        messagebox.showinfo("Ha votado con exito","su voto " + listas[voto-1] + " se registro correctamente")
        ventana.destroy()

#menú
op = 'M'

def mostrarVentana():
    raiz = Tk()
    raiz.title("Votar")
    raiz.config(bg = "navyblue")
    raiz.geometry("600x400")
    raiz.resizable (0,0)
    img = PhotoImage(file="normal.gif")
    widget = Label(raiz, image=img).grid(row=0, column=0)
    vp = Frame (raiz)

    vp.grid (column=0, row=0, padx=(200,250), pady=(20,20))
    vp.columnconfigure (0, weight=1)
    vp.rowconfigure(0, weight=1)

    etiqueta = Label(vp, text="VOTAR",
    font=("Times New Roman", 20), fg="navyblue",)
    etiqueta.grid(row=1, column=0)

    b1=Button(vp,text="Lista 1 ", font=("Times New Roman", 12), fg="black",bg ="white",
    command=lambda:registrarVoto(1, raiz))
    b1.grid(row=2, column=0)

    b2=Button(vp,text="Lista 2 ", font=("Times New Roman", 12), fg="black",bg ="white",
    command=lambda:registrarVoto(2, raiz))
    b2.grid(row=3, column=0)

    b3=Button(vp,text="Lista 3 ", font=("Times New Roman", 12), fg="black",bg ="white",
    command=lambda:registrarVoto(3, raiz))
    b3.grid(row=4, column=0)

    b4=Button(vp,text=" Voto en Blanco ", font=("Times New Roman", 12), fg="black",bg ="white",
    command=lambda:registrarVoto(4, raiz))
    b4.grid(row=5, column=0)

    raiz.mainloop()

def respuestaGuiVotar():
    global op
    mostrarVentana()
    return op
