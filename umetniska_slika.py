def umetniska_slika():   
    import tkinter as tk
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=650, height=450)
    platno.pack()

    platno.create_line(0, 0, 100, 200)
    platno.create_rectangle(300, 250, 550, 350, fill='red')
    platno.create_oval(100, 300, 200, 400)
    platno.create_polygon(350, 50, 450, 50, 450, 250, outline='green', fill='blue')
    platno.create_text(250, 150, text='Umetniška slika', fill='red', font=('Arial', 30))
    okno.mainloop()
