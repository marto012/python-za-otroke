import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 6:
        martin.forward(50)
        martin.left(360/6)
        i = i + 1

    martin.hideturtle()
    turtle.done()


naloga_1()
