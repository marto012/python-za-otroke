import time
import tkinter as tk
from random import randint


def naloga_1():
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=400)
    platno.pack()

    krogec = platno.create_oval(0, 0, 30, 30, fill='orange')

    i = 1
    while i <= 100:
        platno.move(krogec, 2, 2)
        okno.update()
        time.sleep(0.05)
        i = i + 1

    okno.mainloop()


def naloga_2():
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=400)
    platno.pack()

    krogec = platno.create_oval(100, 100, 130, 130, fill='blue')

    def levo():
        platno.move(krogec, -2, 0)
        okno.update()
        time.sleep(0.2)

    def desno():
        platno.move(krogec, 2, 0)
        okno.update()
        time.sleep(0.2)

    def gor():
        platno.move(krogec, 0, -2)
        okno.update()
        time.sleep(0.2)

    def dol():
        platno.move(krogec, 0, 2)
        okno.update()
        time.sleep(0.2)

    i = 1
    while i <= 100:
        desno()
        i = i + 1

    i = 1
    while i <= 50:
        dol()
        i = i + 1

    i = 1
    while i <= 50:
        desno()
        i = i + 1

    i = 1
    while i <= 50:
        dol()
        i = i + 1

    i = 1
    while i <= 150:
        levo()
        i = i + 1

    i = 1
    while i <= 100:
        gor()
        i = i + 1

    okno.mainloop()


def naloga_3():
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=600)
    platno.pack()

    krogec = platno.create_oval(300, 300, 330, 330, fill='blue')

    i = 1
    while i <= 10:
        okno.update()
        time.sleep(0.2)
        x = randint(-200, 200)
        y = randint(-200, 200)
        platno.move(krogec, x, y)
        i = i + 1

    okno.mainloop()


if __name__ == "__main__":
     naloga_3()
