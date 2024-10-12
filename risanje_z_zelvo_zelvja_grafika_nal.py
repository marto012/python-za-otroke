import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()

    martin.forward(100)
    martin.backward(50)
    martin.up()
    martin.right(90)
    martin.forward(50)
    martin.down()
    martin.setheading(0)
    martin.forward(100)
    martin.hideturtle()

    turtle.done()


def naloga_2():
    martin = turtle.Pen()
    martin.reset()

    martin.color('red')
    martin.begin_fill()
    martin.forward(20)
    martin.left(90)
    martin.forward(100)
    martin.left(90)
    martin.forward(20)
    martin.left(90)
    martin.forward(100)
    martin.end_fill()
    martin.up()
    martin.backward(100)
    martin.setheading(0)
    martin.forward(10)
    martin.down()
    martin.color('yellow')
    martin.begin_fill()
    martin.circle(15)
    martin.end_fill

    turtle.done()

naloga_2()