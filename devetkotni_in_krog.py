import turtle


def devetkotnik():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 9:
        martin.forward(50)
        martin.left(360 / 9)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def krog():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 120:
        martin.forward(3)
        martin.left(360 / 120)
        i = i + 1

    martin.hideturtle()
    turtle.done()
