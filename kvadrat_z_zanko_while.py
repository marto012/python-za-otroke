import turtle


def kvadrat_z_zanko_while():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 4:
        martin.forward(50)
        martin.left(90)
        i = i + 1

    turtle.done()
