import tkinter as tk

#Ventana
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Listbox \U0001F4C3")

#lista de opciones
colores=["yellow", "red", "blue", "green"]

#Funciones
def mostrarEstado(funcion, valor):
    val=valor.get(valor.curselection())
    funcion.config(text=f"Seleccionaste: {val}")
    ventana.config(
        bg=f"{val}"
    )

#Caja de lista
lista=tk.Listbox(ventana, width=20, height=5, selectmode="single")
for i in colores:
    lista.insert(tk.END,i)
lista.pack(pady=5)

#boton
btn_seleccion=tk.Button(ventana, text="Mostrar seleccion del usuario", command=lambda:mostrarEstado(lbl_resultado, lista))
btn_seleccion.pack(pady=5)

#resultado
lbl_resultado=tk.Label(ventana, text="")
lbl_resultado.pack(pady=5)


ventana=tk.mainloop()