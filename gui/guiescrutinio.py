from tkinter import *

import pymysql
op = 'M'
lista1=0
lista2=0
lista3=0
votoEnBlanco=0

def setOp(opcion, ventana):
    global op
    op = opcion
    ventana.destroy()

def escrutinio():
    global lista1, lista2, lista3, votoEnBlanco
    lista1 = 0
    lista2 = 0
    lista3 = 0
    votoEnBlanco = 0
    conect= pymysql.connect(host="localhost",user="root",passwd="12345",db="votacion")
    cursor = conect.cursor()
    cursor.execute("SELECT * FROM votacion.votos;")

    for linea in cursor:

        if linea[1] == 1:
            lista1=lista1 + 1
        if linea[1] == 2:
            lista2=lista2 + 1
        if linea[1] == 3:
            lista3=lista3 + 1
        if linea[1] == 4:
            votoEnBlanco=votoEnBlanco + 1


    cursor.close()
    conect.close()

def reduccion(cuenta):
    return str(round(cuenta, 2))

def mostrarVentana():
        escrutinio()
        raiz = Tk()
        raiz.title("Escrutinio")
        raiz.config()
        raiz.geometry("600x400")
        raiz.resizable (0,0)
        img = PhotoImage(file="normal.gif")
        widget = Label(raiz, image=img).grid(row=0, column=0)
        vp = Frame (raiz)

        vp.grid (column=0, row=0, padx=(100,100), pady=(20,20))
        vp.columnconfigure (0, weight=1)
        vp.rowconfigure(0, weight=1)

        total=lista1+lista2+lista3+votoEnBlanco
        if total == 0:
            textEtiqueta17 =  "No hay votos registrados"
            total = 1
        else :
            textEtiqueta17 =  "total: " + str(total) + " votos escrutados"

        etiqueta1 = Label(vp, text="ESCRUTINIO",
        font=("Times New Roman", 16), fg="navyblue",)
        etiqueta1.grid(row=0, column=3)


        etiqueta2 = Label(vp, text="LISTA ",
        font=("Times New Roman", 14), fg="navyblue",)
        etiqueta2.grid(row=1, column=0)

        etiqueta3 = Label(vp, text="TOTAL VOTOS ",
        font=("Times New Roman", 14), fg="navyblue",)
        etiqueta3.grid(row=1, column=3)

        etiqueta4 = Label(vp, text="% VOTOS ",
        font=("Times New Roman", 14), fg="navyblue",)
        etiqueta4.grid(row=1, column=6)

        etiqueta5 = Label(vp, text="Lista 1 ",
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta5.grid(row=2, column=0)

        etiqueta6 = Label(vp, text=str(lista1),
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta6.grid(row=2, column=3)

        etiqueta7 = Label(vp, text= reduccion(lista1*100/total),
        font=("Times New Roman", 12), fg="navyblue", )
        etiqueta7.grid(row=2, column=6)

        etiqueta8 = Label(vp, text="Lista 2 ",
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta8.grid(row=3, column=0)

        etiqueta9 = Label(vp, text=str(lista2),
        font=("Times New Roman", 12), fg="navyblue" ,)
        etiqueta9.grid(row=3, column=3)

        etiqueta10 = Label(vp, text=reduccion(lista2*100/total),
        font=("Times New Roman", 12), fg="navyblue" ,)
        etiqueta10.grid(row=3, column=6)

        etiqueta11 = Label(vp, text="Lista 3 ",
        font=("Times New Roman", 12), fg="navyblue", )
        etiqueta11.grid(row=4, column=0)

        etiqueta12 = Label(vp, text=str(lista3),
        font=("Times New Roman", 12), fg="navyblue" ,)
        etiqueta12.grid(row=4, column=3)

        etiqueta13 = Label(vp, text=reduccion(lista3*100/total),
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta13.grid(row=4, column=6)

        etiqueta14 = Label(vp, text="en Blanco",
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta14.grid(row=5, column=0)

        etiqueta15 = Label(vp, text=str(votoEnBlanco),
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta15.grid(row=5, column=3)

        etiqueta16 = Label(vp, text=reduccion(votoEnBlanco*100/total),
        font=("Times New Roman", 12), fg="navyblue",)
        etiqueta16.grid(row=5, column=6)

        etiqueta17 = Label(vp, text=textEtiqueta17,
        font=("Times New Roman", 12), fg="white", bg= "navyblue")
        etiqueta17.grid(row=6)


        #vp.grid(row=6, column=1, columnspan=3)


        raiz.mainloop()



def respuestaGuiEscrutinio():
    mostrarVentana()
    return op
