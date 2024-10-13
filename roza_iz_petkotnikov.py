import turtle


def roza_iz_petkotnikov():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    while j <= 6:
        i = 1
        while i <= 5:
            martin.forward(50)
            martin.right(360 / 5)
            i = i + 1
        martin.right(60)
        j = j + 1
    martin.hideturtle()
    turtle.done()
