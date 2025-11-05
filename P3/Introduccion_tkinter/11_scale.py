import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Scale \U0001F50D")

#Variables dadas
valor=tk.IntVar()

#escalas
scale=tk.Scale(ventana, )

#Funciones
def mostrarEstado(funcion,val):
    funcion.config(text=f"Valor seleccionado por el usuario: {val.get()}")

#boton
btn_confirmacion=tk.Button(ventana, text="Confirmar", command=lambda:mostrarEstado(lbl_resultado,valor))
btn_confirmacion.pack(pady=5)

#resultado
lbl_resultado=tk.Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana=tk.mainloop()