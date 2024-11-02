def klikni():  
    import tkinter as tk

    okno = tk.Tk()
    okno.title("Gumb za kliknit.")

    def pozdrav():
        print("Živjo, kako si kaj?")

    gumb = tk.Button(okno, text="Klikni", command=pozdrav)
    gumb.pack()
    okno.mainloop()
