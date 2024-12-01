def premikajoca_riba():    
    import time
    import tkinter as tk
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=800, height=400)
    platno.pack()

    telo = platno.create_oval(100, 100, 200, 140, fill='blue')
    oko = platno.create_oval(170, 110, 180, 120, fill='yellow')
    rep = platno.create_polygon(100, 120, 80, 100, 80, 140, fill='blue')

    def premik_v_desno():
        platno.move(telo, 5, 0)
        platno.move(oko, 5, 0)
        platno.move(rep, 5, 0)

    i = 1
    while i <= 100:
        premik_v_desno()
        okno.update()
        time.sleep(0.02)
        i = i + 1

    okno.mainloop()
