def premikajoc_kvadratek():
    import time
    import tkinter as tk

    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=600)
    platno.pack()
    kvadratek = platno.create_rectangle(100, 100, 150, 150, fill='blue')

    okno.update()
    time.sleep(2.00)
    platno.move(kvadratek, 200, 0)

    okno.update()
    time.sleep(2.00)
    platno.move(kvadratek, 0, 200)

    okno.update()
    time.sleep(2.00)
    platno.move(kvadratek, -200, -200)

    okno.mainloop()

