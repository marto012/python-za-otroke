import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 6:
        martin.forward(50)
        martin.left(360 / 6)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_2():
    martin = turtle.Pen()
    martin.reset()
    i = 1
    martin.up()
    martin.goto(-50, 50)
    martin.down()

    while i <= 5:
        martin.forward(50)
        martin.up()
        martin.forward(10)
        martin.down()
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_3():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 6:
        martin.forward(50)
        martin.backward(50)
        martin.right(60)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_4a():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 5:
        martin.forward(50)
        martin.left(720 / 5)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_4b():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 8:
        martin.forward(50)
        martin.left(1080 / 8)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_5():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 5:
        martin.left(90)
        martin.forward(50)
        martin.right(90)
        martin.forward(50)
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_6():
    martin = turtle.Pen()
    martin.reset()
    dolzina = 50
    i = 1
    martin.up()
    martin.goto(-100, -100)
    martin.down()

    while i <= 10:
        martin.left(90)
        martin.forward(dolzina)
        martin.right(90)
        martin.forward(dolzina)
        dolzina = dolzina - 5
        i = i + 1

    martin.hideturtle()
    turtle.done()
    
