import tkinter as tk

#Ventana
ventana=tk.Tk()

ventana.geometry("800x600") #Comando para poner el tamaño de la ventana
ventana.title("Marcos o Frame en tkinter \U0001F525\U0001F525\U0001F525")
#ventana.resizable(False,False) #Evita la modificación del tamaño de la ventana

#marcos
marco1=tk.Frame(ventana, width=600, height=400, bg="#1298ef", relief="solid", border=2) #hay más funciones dentro del frame
marco1.pack_propagate(False) #Evita que se modifique el estilo del marco original
marco1.pack(pady=100) #Comando para que se dibuje o muestre dentro de la ventana

marco2=tk.Frame(marco1, width=300, height=150, bg="#BBB930", relief="groove", border=10).pack(pady=150) #forma 2

#fin de la ventana
ventana=tk.mainloop()