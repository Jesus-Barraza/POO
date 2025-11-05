import tkinter as tk

ventana=tk.Tk()
ventana.geometry("600x400")
ventana.title("Textos \U0001F602")

#Función de escritura
def escribir(texto, etiqueta):
    etiqueta.config(
        text=f"{texto}".strip(),
        font=("arial",12)
    )

#titulo
lbl_titulo=tk.Label(ventana, text="Escriba su comentario: ")
lbl_titulo.config(
    font=("arial, 14")
)
lbl_titulo.pack(anchor="n", pady=5)

#texto de comentario
    #caja de texto
txt_texto=tk.Text(ventana)
txt_texto.config(
    width=40,
    height=5
)
txt_texto.pack()
#boton
btn_texto=tk.Button(ventana, text="Mostrar comentario", command=lambda:escribir(txt_texto.get("1.0", tk.END), lbl_texto))
btn_texto.config(
    width=15
)
btn_texto.pack(pady=5)
#etiqueta
lbl_texto=tk.Label(ventana, text="")
lbl_texto.pack()

ventana=tk.mainloop()
