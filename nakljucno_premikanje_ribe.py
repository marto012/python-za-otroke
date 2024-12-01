def premikajoca_riba():    
    import time
    import tkinter as tk
    from random import randint
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=800, height=400)
    platno.pack()

    telo = platno.create_oval(100, 100, 200, 140, fill='blue')
    oko = platno.create_oval(170, 110, 180, 120, fill='yellow')
    rep = platno.create_polygon(100, 120, 80, 100, 80, 140, fill='blue')

    def premik_v_desno(x, y):
        platno.move(telo, x, y)
        platno.move(oko, x, y)
        platno.move(rep, x, y)

    premik_v_desno(300, 100)

    i = 1
    x = 5
    y = 5
    while i <= 1000:
        if i % 10 == 0:
            x = randint(-5, 5)
            y = randint(-5, 5)
        premik_v_desno(x, y)
        okno.update()
        time.sleep(0.03)
        i = i + 1

    okno.mainloop()
