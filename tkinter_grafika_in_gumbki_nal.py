import tkinter as tk
from random import randint


def naloga_1():
    okno = tk.Tk()
    okno.title('2 x 3')

    def izračun():
        print('2 x 3 = 6')

    gumb = tk.Button(okno, text='2 x 3', command=izračun)
    gumb.pack()
    okno.mainloop()


def naloga_2():
    okno = tk.Tk()
    okno.title('PUJSEK')
    platno = tk.Canvas(okno, height=300, width=300)
    platno.pack()

    def pujsek():
        platno.create_oval(100, 100, 200, 200, outline='red', fill='pink')
        platno.create_oval(120, 120, 140, 140, outline='red', fill='white')
        platno.create_oval(160, 120, 180, 140, outline='red', fill='white')
        platno.create_oval(130, 150, 170, 180, outline='red', fill='pink')

    gumb = tk.Button(okno, text='PUJSEK', command=pujsek)
    gumb.pack()
    okno.mainloop()


def naloga_3():
    okno = tk.Tk()
    okno.title('nebo')
    platno = tk.Canvas(okno, width=800, height=600, bg='blue')
    platno.pack()

    def krogec(x, y):
        x1 = x
        y1 = y
        x2 = x1 + 20
        y2 = y1 + 20
        platno.create_oval(x1, y1, x2, y2, fill='yellow')

    i = 1
    while i <= 50:
        x = randint(0, 780)
        y = randint(0, 580)
        krogec(x, y)
        i = i + 1

    okno.mainloop()
