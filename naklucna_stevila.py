def naklucna_stevila(): 
    from random import randint
    import time
    import tkinter as tk
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=400, height=300)
    platno.pack()

    platno.create_text(150, 50, text='Naključna števila:', font=('Arial', 20))
    stevilo = platno.create_text(280, 50, text='0', font=('Arial', 20))

    i = 1
    while i <= 10:
        naklucno_stevilo = randint(1, 6)
        platno.itemconfig(stevilo, text=str(naklucno_stevilo))
        i = i + 1
        okno.update()
        time.sleep(1.00)
