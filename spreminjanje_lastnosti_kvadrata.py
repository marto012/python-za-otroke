import time
import tkinter as tk
okno = tk.Tk()
platno = tk.Canvas(okno, width=500, height=400)
platno.pack()

napis = platno.create_text(100, 100, font=('Arial', 15), text='Rdeč kvadrat')
kvadrat = platno.create_rectangle(100, 150, 150, 200, fill='Red')

okno.update()
time.sleep(2.00)

platno.itemconfig(napis, text='Moder kvadrat')
platno.itemconfig(kvadrat, fill='blue')

okno.mainloop()
