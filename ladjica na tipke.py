import time
import tkinter as tk


def ladjica_na_tipke():

    okno = tk.Tk()
    platno = tk.Canvas(okno, width=500, height=400)
    platno.pack()

    ladjica = platno.create_polygon(120, 200, 130, 220, 170, 220, 180, 200, fill='blue')

    def premik(event):
        smer = 1
        while True:
            polozaj_ladjica = platno.coords(ladjica)
            if polozaj_ladjica[6] > 500 or polozaj_ladjica[0] < 0:
                smer = -smer
            platno.move(ladjica, smer*5, 0)
            okno.update()
            time.sleep(0.05)
    
    platno.bind_all('<KeyPress-a>', premik)

    okno.mainloop()


if __name__ == '__main__':
    ladjica_na_tipke()
