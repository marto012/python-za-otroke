import turtle


def kvadrat_poljubne_velikosti(velikost):
    martin = turtle.Pen()
    martin.reset()

    def kvadrat(velikost):
        i = 1
        while i <= 4:
            martin.forward(velikost)
            martin.right(90)
            i = i + 1

        martin.hideturtle()
        turtle.done()

    kvadrat(velikost)
