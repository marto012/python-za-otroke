import turtle


def kvadrati_v_kvadratih():
    martin = turtle.Pen()
    martin.reset()
    i = 1
    velikost = 20

    while i <= 5:
        j = 1
        while j <= 4:
            martin.forward(velikost)
            martin.left(360/4)
            j = j + 1
        velikost = velikost + 20
        i = i + 1

    martin.hideturtle()
    turtle.done()
