import turtle


def kvadrati_v_vrsti():
    martin = turtle.Pen()
    martin.reset()
    i = 1

    while i <= 8:
        j = 1
        while j <= 4:
            martin.forward(20)
            martin.left(360 / 4)
            j = j + 1
        martin.up()
        martin.forward(30)
        martin.down()
        i = i + 1

    martin.hideturtle()
    turtle.done()
