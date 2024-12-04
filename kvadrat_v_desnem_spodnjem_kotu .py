import tkinter as tk

okno = tk.Tk()
platno = tk.Canvas(okno, width=500, height=400)
platno.pack()

kvadrat = platno.create_rectangle(100, 100, 100 + 50, 100 + 50, fill='orange')


def sredina(event):
    platno.coords(kvadrat, 450, 350, 450 + 50, 350 + 50)


platno.bind_all('<KeyPress-space>', sredina)

okno.mainloop()