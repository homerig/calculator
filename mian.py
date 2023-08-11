
from tkinter import ttk
from tkinter import * 
import math

def TemaSakura(*args): ### ERRORES A CORREGIR CON EL CAMBIO DE TEMAS 
    estilos.configure('mainframe.TFrame', background= '#FFE7F6')
    estilos_label1.configure("Label1.TLabel", background ='#FFC0CB', foreground= '#FF99DE')
    estilos_Label2.configure("Label2.TLabel", background ='#FFC0CB', foreground= '#FF99DE')
    estilos_botones_numeros.configure('botones_numeros.TButton', background= '#FFC0CB', foreground= '#F52BC0')
    estilos_botones_borrar.configure("botones_borrar.TButton", background='#FC8DC0',foreground='#F52BC0')
    estilos_botones_restantes.configure("botones_restantes.TButton", background='#FC8DC0', foreground='#F52BC0')

def TemaDefault(*args):
    pass

root = Tk()
root.title("Calculadora")
root.geometry("+500+100")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)


estilos = ttk.Style()
estilos.configure('mainframe.TFrame',background = "#DBDBDB")
estilos.theme_use("clam")

# mainframe de la calculadora 
mainframe = ttk.Frame(root, style = 'mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W,E,N,S))
for i in range(4):
    mainframe.columnconfigure(i,weight=1)
for i in range(7):
    mainframe.rowconfigure(i,weight=1)

#Estilos Labels
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font="arial 15", anchor="e")

estilos_Label2 = ttk.Style()
estilos_Label2.configure("Label2.TLabel", font="arial 40", anchor="e")

#LABEL 1
entrda1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrda1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,E,N,S))

#LABEL 2
entrda2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrda2, style= "Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,E,N,S))

# Estilos Botones

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("botones_numeros.TButton", font= "arial 22", width=5, background = "#FFFFFF", relief = "flat")
estilos_botones_numeros.map("botones_numeros.TButton", background=[("active", "#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("botones_borrar.TButton", font= "arial 22", width=5, background = "#CECECE", relief = "flat")
estilos_botones_borrar.map("botones_borrar.TButton", foreground=[("active", "#FF0000")], background =[("active","#858585")])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure("botones_restantes.TButton", font= "arial 22", width=5, background = "#CECECE", relief = "flat")
estilos_botones_restantes.map("botones_restantes.TButton", background=[("active", "#B9B9B9")])

# Botones numeros 
button0 = ttk.Button(mainframe, text = "0", style="botones_numeros.TButton")
button1 = ttk.Button(mainframe, text = "1", style="botones_numeros.TButton")
button2 = ttk.Button(mainframe, text = "2", style="botones_numeros.TButton")
button3 = ttk.Button(mainframe, text = "3", style="botones_numeros.TButton")
button4 = ttk.Button(mainframe, text = "4", style="botones_numeros.TButton")
button5 = ttk.Button(mainframe, text = "5", style="botones_numeros.TButton")
button6 = ttk.Button(mainframe, text = "6", style="botones_numeros.TButton")
button7 = ttk.Button(mainframe, text = "7", style="botones_numeros.TButton")
button8 = ttk.Button(mainframe, text = "8", style="botones_numeros.TButton")
button9 = ttk.Button(mainframe, text = "9", style="botones_numeros.TButton")

# Botones de operacion
button_coma = ttk.Button(mainframe, text = ",",style="botones_restantes.TButton")
button_borrar = ttk.Button(mainframe, text = chr(9003),style="botones_borrar.TButton")
button_borrar_todo = ttk.Button(mainframe, text = "C",style="botones_borrar.TButton")
button_abrir_parentesis = ttk.Button(mainframe, text = "(",style="botones_restantes.TButton")
button_cerrar_parentesis = ttk.Button(mainframe, text = ")",style="botones_restantes.TButton")

button_division = ttk.Button(mainframe, text=chr(247),style="botones_restantes.TButton")
button_multplicidad = ttk.Button(mainframe, text="x",style="botones_restantes.TButton")
button_suma = ttk.Button(mainframe, text="+",style="botones_restantes.TButton")
button_resta = ttk.Button(mainframe, text="-",style="botones_restantes.TButton")
button_igual = ttk.Button(mainframe, text="=",style="botones_restantes.TButton")
button_raiz_cuadrada = ttk.Button(mainframe, text="√",style="botones_restantes.TButton")

# poner botones en la pantalla 
button_abrir_parentesis.grid(column=0,row=2,sticky=(W,E,N,S))
button_cerrar_parentesis.grid(column=1,row=2,sticky=(W,E,N,S))
button_borrar_todo.grid(column=2,row=2,sticky=(W,E,N,S))
button_borrar.grid(column=3,row=2,sticky=(W,E,N,S))

button7.grid(column=0,row=3,sticky=(W,E,N,S))
button8.grid(column=1,row=3,sticky=(W,E,N,S))
button9.grid(column=2,row=3,sticky=(W,E,N,S))
button_division.grid(column=3,row=3,sticky=(W,E,N,S))

button4.grid(column=0,row=4,sticky=(W,E,N,S))
button5.grid(column=1,row=4,sticky=(W,E,N,S))
button6.grid(column=2,row=4,sticky=(W,E,N,S))
button_multplicidad.grid(column=3,row=4,sticky=(W,E,N,S))

button1.grid(column=0,row=5,sticky=(W,E,N,S))
button2.grid(column=1,row=5,sticky=(W,E,N,S))
button3.grid(column=2,row=5,sticky=(W,E,N,S))
button_suma.grid(column=3,row=5,sticky=(W,E,N,S))

button0.grid(column=0,row=6,columnspan=2,sticky=(W,E,N,S))
button_coma.grid(column=2,row=6,sticky=(W,E,N,S))
button_resta.grid(column=3,row=6,sticky=(W,E,N,S))

button_igual.grid(column=0,row=7,columnspan=3,sticky=(W,E,N,S))
button_raiz_cuadrada.grid(column=3,row=7,sticky=(W,E,N,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-s>', TemaSakura)

root.mainloop()