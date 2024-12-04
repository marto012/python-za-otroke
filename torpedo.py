import tkinter as tk
okno = tk.Tk()
platno = tk.Canvas(okno, height=400, width=800)
platno.pack()

torpedo = platno.create_oval(200, 200, 270, 230, fill='brown')


def premik_torpeda(event):
    if event.keysym == 'Up':
        platno.move(torpedo, 0, -5)
    
    elif event.keysym == 'Down':
        platno.move(torpedo, 0, 5)
     
    elif event.keysym == 'Left':
        platno.move(torpedo, -5, 0)

    else:
        platno.move(torpedo, 5, 0)


platno.bind_all('<KeyPress-Up>', premik_torpeda)
platno.bind_all('<KeyPress-Down>', premik_torpeda)
platno.bind_all('<KeyPress-Left>', premik_torpeda)
platno.bind_all('<KeyPress-Right>', premik_torpeda)

okno.mainloop()
