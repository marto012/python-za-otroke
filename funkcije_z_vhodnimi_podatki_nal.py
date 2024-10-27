import turtle


martin = turtle.Pen()
martin.reset()


def naloga_1(velikost):
    def vrh(velikost):
        martin.left(60)
        martin.forward(velikost)
        martin.right(360 / 3)
        martin.forward(velikost)
        martin.left(60)

    vrh(velikost)


def naloga_2(velikost_kvadrata):
    i = 1

    def kvadrat(velikost_kvadrata):
        j = 1
        while j <= 4:
            martin.forward(velikost_kvadrata)
            martin.left(90)
            j = j + 1

    while i <= 4:
        kvadrat(velikost_kvadrata)
        martin.up()
        martin.forward(velikost_kvadrata + 10)
        martin.down()
        velikost_kvadrata = velikost_kvadrata + 20
        i = i + 1

    martin.hideturtle()
    turtle.done()


def naloga_3(stevilo_kvadratov):
    j = 1

    def kvadrat():
        i = 1
        while i <= 4:
            martin.forward(20)
            martin.left(90)
            i = i + 1

    while j <= stevilo_kvadratov:
        kvadrat()
        martin.up()
        martin.forward(30)
        martin.down()
        j = j + 1

    martin.hideturtle()
    turtle.done()

