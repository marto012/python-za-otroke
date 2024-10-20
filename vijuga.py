import turtle


def vijuga():
    martin = turtle.Pen()
    martin.reset()

    def polkrogD():
        i = 1
        while i <= 18:
            martin.forward(2)
            martin.right(360/36)
            i = i + 1
  
    def polkrogL():
        i = 1
        while i <= 18:
            martin.forward(2)
            martin.left(360/36)
            i = i + 1

    j = 1
    martin.left(90)
    while j <= 5:
        polkrogD()
        polkrogL()
        j = j + 1

    martin.hideturtle()
    turtle.done()


