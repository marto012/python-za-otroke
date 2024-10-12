import turtle


def risanje_po_koordinatah():
    martin = turtle.Pen()
    martin.reset()

    martin.up()
    martin.goto(100, 100)
    martin.down()
    martin.goto(200, 100)
    martin.goto(200, 200)
    martin.goto(100, 200)
    martin.goto(100, 100)

    turtle.done()
