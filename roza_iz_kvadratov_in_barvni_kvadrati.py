import turtle


def roza_iz_kvadratov_in_barvni_kvadrati():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    def kvadrat():
        i = 1

        while i <= 4:
            martin.forward(50)
            martin.right(90)
            i = i + 1

    while j <= 6:
        kvadrat()
        martin.right(60)
        j = j + 1

    martin.up()
    martin.forward(150)
    martin.down()

    martin.pensize(3)
    martin.color("red")
    kvadrat()
    martin.right(120)
    martin.color("yellow")
    kvadrat()
    martin.right(120)
    martin.color("cyan")
    kvadrat()

    martin.hideturtle()
    turtle.done()
