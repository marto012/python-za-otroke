import turtle


def kvadratki_v_vrsti():
    martin = turtle.Pen()
    martin.reset()

    def kvadratek():
        i = 1
        while i <= 4:
            martin.forward(20)
            martin.left(90)
            i = i + 1

    j = 1
    while j <= 8:
        kvadratek()
        martin.up()
        martin.forward(30)
        martin.down()
        j = j + 1

    martin.hideturtle()
    turtle.done()

