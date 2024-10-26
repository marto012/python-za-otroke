import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    def sestkotnik():
        i = 1
        while i <= 6:
            martin.forward(50)
            martin.right(360 / 6)
            i = i + 1

    while j <= 2:
        sestkotnik()
        j = j + 1
        martin.left(120)

    martin.hideturtle()
    turtle.done()


def naloga_2():
    martin = turtle.Pen()
    martin.reset()

    def trikotnik():
        martin.begin_fill()
        i = 1

        while i <= 3:
            martin.forward(50)
            martin.right(360 / 3)
            i = i + 1

        martin.end_fill()

    martin.color("red")
    trikotnik()
    martin.right(60)
    martin.color("yellow")
    trikotnik()
    martin.right(60)
    martin.color("cyan")
    trikotnik()
    martin.right(60)
    martin.color("red")
    trikotnik()
    martin.right(60)
    martin.color("yellow")
    trikotnik()
    martin.right(60)
    martin.color("cyan")
    trikotnik()
    martin.right(60)

    martin.hideturtle()
    turtle.done()


def naloga_3():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    def stopnica():
        martin.left(90)
        martin.forward(10)
        martin.right(90)
        martin.forward(10)

    while i <= 10:
        stopnica()
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_4():
    martin = turtle.Pen()
    martin.reset()

    def cetertina():
        i = 1
        while i <= 30:
            martin.forward(3)
            martin.right(360 / 120)
            i = i + 1

    j = 1

    while j <= 5:
        cetertina()
        martin.right(90)
        cetertina()
        martin.right(90)
        martin.right(360 / 5)
        j = j + 1

    martin.hideturtle()
    turtle.done()


def naloga_5():
    martin = turtle.Pen()
    martin.reset()

    def polkrogD():
        p = 1
        while p <= 18:
            martin.forward(2)
            martin.right(360/36)
            p = p + 1

    j = 1
    martin.left(90)
    while j <= 5:
        polkrogD()
        martin.left(180)
        polkrogD()
        martin.left(90)
        martin.up()
        martin.forward(20)
        martin.down()
        martin.left(90)
        j = j + 1
 
    martin.hideturtle()
    turtle.done()
