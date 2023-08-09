import tkinter
from tkinter import ttk
from tkinter import * 
import math

root = Tk()
root.title("Calculadora")
root.geometry("+500+100")


estilos = ttk.Style()
estilos.configure('mainframe.TFrame',background = "#DBDBDB")


mainframe = ttk.Frame(root, style = 'mainframe.TFrame')
mainframe.grid(column=0, row=0)

#LABEL 1
entrda1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrda1)
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,E))

#LABEL 2
entrda2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrda2)
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,E))

# Botones numeros 
button0 = ttk.Button(mainframe, text = "0")
button1 = ttk.Button(mainframe, text = "1")
button2 = ttk.Button(mainframe, text = "2")
button3 = ttk.Button(mainframe, text = "3")
button4 = ttk.Button(mainframe, text = "4")
button5 = ttk.Button(mainframe, text = "5")
button6 = ttk.Button(mainframe, text = "6")
button7 = ttk.Button(mainframe, text = "7")
button8 = ttk.Button(mainframe, text = "8")
button9 = ttk.Button(mainframe, text = "9")

# Botones de operacion
button_coma = ttk.Button(mainframe, text = ",")
button_borrar = ttk.Button(mainframe, text = chr(9003))
button_borrar_todo = ttk.Button(mainframe, text = "C")
button_abrir_parentesis = ttk.Button(mainframe, text = "(")
button_cerrar_parentesis = ttk.Button(mainframe, text = ")")

button_division = ttk.Button(mainframe, text=chr(247))
button_multplicidad = ttk.Button(mainframe, text="x")
button_suma = ttk.Button(mainframe, text="+")
button_resta = ttk.Button(mainframe, text="-")
button_igual = ttk.Button(mainframe, text="=")
button_raiz_cuadrada = ttk.Button(mainframe, text="√")

# poner botones en la pantalla 
button_abrir_parentesis.grid(column=0,row=2)
button_cerrar_parentesis.grid(column=1,row=2)
button_borrar_todo.grid(column=2,row=2)
button_borrar.grid(column=3,row=2)
button7.grid(column=0,row=4)
button8.grid(column=1,row=4)
button9.grid(column=2,row=4)
button_division.grid(column=3,row=4)

button4.grid(column=0,row=5)
button5.grid(column=1,row=5)
button6.grid(column=2,row=5)
button_multplicidad.grid(column=3,row=5)

button1.grid(column=0,row=6)
button2.grid(column=1,row=6)
button3.grid(column=2,row=6)
button_suma.grid(column=3,row=6)

button0.grid(column=0,row=7,columnspan=2,sticky=(W,E))
button_coma.grid(column=2,row=7)
button_resta.grid(column=3,row=7)

button_igual.grid(column=0,row=8,columnspan=3,sticky=(W,E))
button_raiz_cuadrada.grid(column=3,row=8)


root.mainloop()