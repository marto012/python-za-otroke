import turtle


def pravokotnik():
    martin = turtle.Pen()  # naredi turtle pen

    martin.forward(100)
    martin.left(90)
    martin.forward(50)
    martin.left(90)
    martin.forward(100)
    martin.left(90)
    martin.forward(50)
    martin.left(90)
    martin.hideturtle()  # skrije želvo na koncu risbe

    turtle.done()
