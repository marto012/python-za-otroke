import turtle
martin = turtle.Pen()


def kvadrat():
    martin.reset()
    i = 1

    while i <= 4:
        martin.forward(50)
        martin.right(90)
        i = i + 1
