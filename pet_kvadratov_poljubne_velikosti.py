import turtle


def pet_kvadratov_poljubne_velikosti(velikost):
    martin = turtle.Pen()
    martin.reset()

    def kvadrat(velikost):
        i = 1
        while i <= 4:
            martin.forward(velikost)
            martin.right(90)
            i = i + 1
    j = 1
    velikost = 20
    while j <= 5:
        kvadrat(velikost)
        velikost = velikost + 20
        j = j + 1

    martin.hideturtle()
    turtle.done()

    kvadrat(velikost)

