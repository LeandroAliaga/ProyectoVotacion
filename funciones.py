# -- coding: utf-8

#FUNCIONES
from os import system, name
import pymysql
from tkinter import *


op=''

def mostrarMenu():
    print (" ---- Menu de sistema de votacion ---- ")
    print ("(V)otar")
    print ("(E)scrutinio")
    print ("(S)alir")
    print ("(B)orrar")


def pedirOpcion():
    op = input("Ingresa la opcion elegida: ")
    return op

def mostrarLista():
    print('/------------------------------------------------/')
    print('')
    print ("Opciones a votar")
    print('')
    print (" (1) Lista 1 ")
    print('')
    print (" (2) Lista 2 ")
    print('')
    print (" (3) Lista 3 ")
    print('')
    print (" (B) Voto en blanco ")
    print('')
    print('/------------------------------------------------/')


def pedirVoto():
    voto = input("Ingresa la lista elegida : ")
    return voto

"""def guardarVoto(voto, lista1, lista2, lista3, votoEnBlanco):

    if (voto == "1"):
        lista1 = lista1 + 1
    if (voto == "2"):
        lista2 = lista2 + 1
    if (voto == "3"):
        lista3 = lista3 + 1
    if (voto == "B"):
        votoEnBlanco = votoEnBlanco + 1
    print("gracias por su voto!")"""

def escrutinio(lista1, lista2, lista3, votoEnBlanco):

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

    print ("lista numero 1: " + str(lista1) + " votos.")
    print ('---------------------------')
    print ("lista numero 2: " + str(lista2) + " votos.")
    print ('---------------------------')
    print ("lista numero 3: " + str(lista3) + " votos.")
    print ('---------------------------')
    print ("votoEnBlanco :" + str(votoEnBlanco) + " votos.")

    cursor.close()
    conect.close()


def clear():
    if name =="nt":
        _= system("cls")
    else:
        _=system("clear")

def registrarVoto(voto):
    conect = pymysql.connect(host="localhost",user="root",passwd="12345",db="votacion")
    cursor = conect.cursor()
    cursor.execute(
        "INSERT INTO votos (idlista,fecha) VALUES (%s, null)",
        (voto)
    )
    conect.commit()
    cursor.close()
    conect.close()



def contarLista1():
    archivo= open("lista1.txt","r")
    voto = 0
    for line in archivo.readlines():
        voto = voto + 1
    archivo.close()
    return voto

def contarLista2():
    archivo= open("lista2.txt","r")
    voto = 0
    for line in archivo.readlines():
        voto = voto + 1
    archivo.close()
    return voto

def contarLista3():
    archivo= open("lista3.txt","r")
    voto = 0
    for line in archivo.readlines():
        voto = voto + 1
    archivo.close()
    return voto

# ----------------------------------------VISTAS

def setOpcion(opcion, ventana):
    global op
    op = opcion
    ventana.destroy()

def cerrarVentana(ventana):
    ventana.destroy()

#cambiar_stringvar(textoentry.get(),mitexto, raiz)

def guiValidarPass():
    raiz = Tk()
    raiz.title("Autenticación")
    raiz.config(bg = "grey")
    raiz.geometry("600x400")
    raiz.resizable(0,0)

    vp = Frame (raiz)

    vp.grid (column=0, row=0, padx=(100,100), pady=(20,20))
    vp.columnconfigure (0, weight=1)
    vp.rowconfigure(0, weight=1)

    etiqueta = Label(vp, text="Autenticación",
    font=("Calibri", 16), fg="black",)
    etiqueta.grid(row=1, column=0)

    etiqueta2 = Label(vp, text="Ingrese la contrasenia del Administrador",
    font=("Calibri", 12), fg="black",)
    etiqueta2.grid(row=2, column=0)

    mitexto=StringVar()
    textoentry=StringVar()
    entry1=Entry(vp ,textvar=textoentry).grid()
    label1=Label(vp ,textvar=mitexto).grid()
    b1=Button(vp, text="autenticar", command=lambda:cerrarVentana(raiz))
    b1.grid()

    raiz.mainloop()

    return textoentry.get()
