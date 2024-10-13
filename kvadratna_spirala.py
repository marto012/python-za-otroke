import turtle


def kvadratna_spirala():
    martin = turtle.Pen()
    martin.reset()
    i = 1
    korak = 2

    while i <= 40:
        martin.forward(korak)
        martin.left(90)
        i = i + 1
        korak = korak + 2

    martin.hideturtle()
    turtle.done()
