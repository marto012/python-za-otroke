import turtle


def barvne_crte():
    martin = turtle.Pen()
    martin.reset()

    martin.color("red")
    martin.forward(50)
    martin.up()
    martin.forward(30)
    martin.down()
    martin.color("green")
    martin.forward(50)
    martin.up()
    martin.forward(30)
    martin.down()
    martin.color("yellow")
    martin.forward(50)
    martin.up()
    martin.forward(30)
    martin.down()
    martin.hideturtle()

    turtle.done()
