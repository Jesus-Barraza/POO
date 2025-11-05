import tkinter as tk

#ventana
ventana=tk.Tk()
ventana.geometry("600x400")
ventana.title("Etiquetas \U0001F940")

#marcos
marco1=tk.Frame(ventana, width=600, height=100, bg="#ffffaa", relief="flat", border=10)
marco1.pack_propagate(False)
marco1.pack()

marco2=tk.Frame(ventana, width=600, height=100, bg="#aaffaa", relief="raised", border=10)
marco2.pack_propagate(False)
marco2.pack()

marco3=tk.Frame(ventana, width=600, height=100, bg="#ffaaaa", relief="solid", border=10)
marco3.pack_propagate(False)
marco3.pack()

marco4=tk.Frame(ventana, width=600, height=100, bg="#aaaaff", relief="sunken", border=10)
marco4.pack_propagate(False)
marco4.pack()


#etiquetas
etiqueta1=tk.Label(marco1, text="Barraza Torres Jesús Daniel", bg="#ffffaa").pack(pady=25)
etiqueta2=tk.Label(marco2, text="Universidad tecnológica de Durango", bg="#aaffaa").pack(pady=25)
etiqueta3=tk.Label(marco3, text="Tecnologías de la información", bg="#ffaaaa").pack(pady=25)
etiqueta4=tk.Label(marco4, text="Desarrollo de software multiplataforma", bg="#aaaaff").pack(pady=25)

ventana=tk.mainloop()