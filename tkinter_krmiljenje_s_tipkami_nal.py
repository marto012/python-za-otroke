def naloga_1():
    import tkinter as tk
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=500, height=500)
    platno.pack()

    glava = platno.create_oval(100, 100, 100 + 50, 100 + 50, 
                               fill='green', outline='black')
    usta = platno.create_arc(110, 110, 140, 140, 
                             start=180, extent=180, style='arc', width=3)

    def premik_smejko(event):
        if event.keysym == 'Left':
            platno.move(glava, -10, 0)
            platno.move(usta, -10, 0)

        else:
            platno.move(glava, 10, 0)
            platno.move(usta, 10, 0)

    platno.bind_all('<Left>', premik_smejko)
    platno.bind_all('<Right>', premik_smejko)

    okno.mainloop()


def naloga_2():
    from random import randint
    import tkinter as tk
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=400, bg='blue')
    platno.pack()

    pravokotnik = platno.create_rectangle(200, 0, 400, 400, fill='pink')
    kvadratek = platno.create_rectangle(100, 100, 100 + 30, 100 + 30, fill='pink', 
                                        outline='black')

    def premik_kvadratka(event):
        x = randint(0, 470)
        y = randint(0, 470)
        if x > 185 and x < 385:
            platno.itemconfig(kvadratek, fill='blue')
        
        else:
            platno.itemconfig(kvadratek, fill='pink')
        
        platno.coords(kvadratek, x, y, x + 30, y + 30)

    platno.bind_all('<Button-1>', premik_kvadratka)
   
    okno.mainloop()


naloga_2()