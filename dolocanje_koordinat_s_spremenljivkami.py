def dolocanje_koordinat_s_spremenkjivkami():
    import tkinter as tk

    okno = tk.Tk()
    platno = tk.Canvas(okno, width=800, height=600)
    platno.pack()

    def kvadratek(x, y):
        x1 = x
        y1 = y
        x2 = x1 + 30
        y2 = y1 + 30
        platno.create_rectangle(x1, y1, x2, y2, fill="red")

    x = 0
    y = 0

    while y < 570:
        kvadratek(x, y)
        x = x + 50
        y = y + 50

    okno.mainloop()


if __name__ == "__main__":
    dolocanje_koordinat_s_spremenkjivkami()
