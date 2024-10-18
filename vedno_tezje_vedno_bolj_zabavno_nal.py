import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    while j <= 12:
        i = 1
        while i <= 4:
            martin.forward(50)
            martin.right(360 / 4)
            i = i + 1
        martin.right(30)
        j = j + 1
    martin.hideturtle()
    turtle.done()


def naloga_2():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    while j <= 8:
        i = 1
        while i <= 4:
            martin.forward(20)
            martin.left(90)
            i = i + 1

        martin.forward(20)
        martin.left(90)
        martin.forward(20)
        martin.right(90)
        j = j + 1

    martin.hideturtle()
    turtle.done()


def naloga_3():
    martin = turtle.Pen()
    martin.reset()
    i = 1
    stranica = 100

    while i <= 5:
        j = 1
        while j <= 4:
            martin.forward(stranica)
            martin.left(90)
            j = j + 1
        stranica = stranica - 20
        martin.up()
        martin.forward(10)
        martin.left(90)
        martin.forward(10)
        martin.right(90)
        martin.down()
        i = i + 1

    turtle.done()
