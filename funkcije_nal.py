import turtle


def naloga_1():
    martin = turtle.Pen()
    martin.reset()
    j = 1

    def sestkotnik():
        i = 1
        while i <= 6:
            martin.forward(50)
            martin.right(360 / 6)
            i = i + 1

    while j <= 2:
        sestkotnik()
        j = j + 1
        martin.left(120)

    martin.hideturtle()
    turtle.done()


def naloga_2():
    martin = turtle.Pen()
    martin.reset()

    def trikotnik():
        martin.begin_fill()
        i = 1
       
        while i <= 3:
            martin.forward(50)
            martin.right(360/3)
            i = i + 1
        
        martin.end_fill()

    martin.color('red')
    trikotnik()
    martin.right(60)
    martin.color('yellow')
    trikotnik()
    martin.right(60)
    martin.color('cyan')
    trikotnik()
    martin.right(60)
    martin.color('red')
    trikotnik()
    martin.right(60)
    martin.color('yellow')
    trikotnik()
    martin.right(60)
    martin.color('cyan')
    trikotnik()
    martin.right(60)

    martin.hideturtle()
    turtle.done()
