import tkinter as tk
import random
import time

okno = tk.Tk()
okno.title('Ladjo upravljaš s puščicami. Izogibaj se črnim krogom, in pobiraj oranžne pravokotnike.')
platno = tk.Canvas(okno, width=800, height=600, bg='blue')
platno.pack()
ladja = platno.create_polygon(410, 480, 420, 500, 500, 500, 510, 480, 
                              470, 480, 470, 460, 430, 465, 430, 480, 
                              outline='black', fill='gray') 
bomba = platno.create_oval(200, 0, 220, 20, outline='orange', fill='black')
padalec = platno.create_rectangle(100, 0, 115, 40, outline='black', fill='orange')
tocke = platno.create_text(650, 30, text='Točke:', font=('Comic Sans MS', 20))
stevilo_tock = platno.create_text(705, 30, text='0', font=('Comic Sans MS', 20))
zivljenja = platno.create_text(660, 70, text='Življenja:', font=('Comic Sans MS', 20))
stevilo_zivljenj = platno.create_text(730, 70, text='3', font=('Comic Sans MS', 20))


polozaj_ladje = platno.coords(ladja)


def premik_ladje(event):
    if event.keysym == 'Left':
        hitrost = -20
        if polozaj_ladje[1] < 0:
            hitrost = 0   
        platno.move(ladja, hitrost, 0)

    else:
        hitrost = 20
        if polozaj_ladje[4] >= 800:
            hitrost = 0
        platno.move(ladja, hitrost, 0)


platno.bind_all('<Left>', premik_ladje)
platno.bind_all('<Right>', premik_ladje)


def premik_padalca():
    platno.move(padalec, 0, hitrost_padalec)


def premik_bomba():
    platno.move(bomba, 0, hitrost_bomba)


def premik_gor_padalec():
    x = random.randint(50, 700)
    platno.coords(padalec, x, 0, x + 15, 40)


def premik_gor_bomba():
    x = random.randint(50, 700)
    platno.coords(bomba, x, 0, x + 15, 20)


def dotik_bomba():
    polozaj_ladje = platno.coords(ladja)
    if polozaj_bomba[3] >= polozaj_ladje[1] and polozaj_bomba[3] <= polozaj_ladje[1]+20:
        if polozaj_bomba[2] >= polozaj_ladje[0] and polozaj_bomba[2] <= polozaj_ladje[6]+20:
            return True
        
        else: 
            return False
        

def dotik_padalec():
    polozaj_ladje = platno.coords(ladja)
    if polozaj_padalec[3] >= polozaj_ladje[1] and polozaj_padalec[3] <= polozaj_ladje[1]+20:
        if polozaj_padalec[2] >= polozaj_ladje[0] and polozaj_padalec[2] <= polozaj_ladje[6]+20:
            return True
        
        else: 
            return False
 

def izpis():
    platno.itemconfig(stevilo_tock, text=str(tocke))
    platno.itemconfig(stevilo_zivljenj, text=str(zivljenja))


tocke = 0
zivljenja = 3
hitrost_padalec = 5
hitrost_bomba = 10

while zivljenja > 0:
    okno.update()
    time.sleep(0.05)
    izpis()
    premik_bomba()
    premik_padalca()
    polozaj_padalec = platno.coords(padalec)
    polozaj_bomba = platno.coords(bomba)
    if polozaj_padalec[1] > 600:
        premik_gor_padalec()

    if dotik_padalec():
        premik_gor_padalec()
        tocke = tocke + 1

    if polozaj_bomba[1] > 600:
        premik_gor_bomba()

    if dotik_bomba():
        premik_gor_bomba()
        zivljenja = zivljenja - 1

    if random.randint(1, 100) == 1:
        hitrost_bomba = hitrost_bomba + 1
        hitrost_padalec = hitrost_padalec + 1

if zivljenja == 0:
    platno.itemconfig(stevilo_zivljenj, text=str(zivljenja))

print('Število doseženih točk:', tocke)
game_over = platno.create_text(400, 300, text='GAME OVER', font=('Comic Sans MS', 100,))
okno.mainloop()