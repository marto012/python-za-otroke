import turtle


# 1. naloga(nal 1)
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


# 2. naloga(nal 2)
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
    martin.end_fill()
    martin.color('black')
    martin.up()
    martin.backward(1)
    martin.begin_fill()
    martin.down()
    martin.forward(2)
    martin.left(90)
    martin.forward(20)
    martin.left(90)
    martin.forward(2)
    martin.left(90)
    martin.forward(20)
    martin.end_fill()
    martin.hideturtle()

    turtle.done()


# 3. naloga(nal 3)
def naloga_3():
    martin = turtle.Pen()
    martin.reset()

    martin.color('orange')
    martin.pensize(5)
    martin.up()
    martin.goto(-100, -100)
    martin.down()
    martin.goto(0, 200)
    martin.goto(100, -100)
    martin.up()
    martin.goto(50, 50)
    martin.down()
    martin.goto(-50, 50)
    martin.hideturtle()

    turtle.done()
