import turtle


def kuzek():
    martin = turtle.Pen()
    martin.reset()

    martin.begin_fill()
    martin.color('brown')
    martin.circle(25)
    martin.end_fill()
    martin.up()
    martin.left(90)
    martin.forward(40)
    martin.left(90)
    martin.forward(10)
    martin.down()
    martin.color('black')
    martin.begin_fill()
    martin.circle(5)
    martin.end_fill()
    martin.up()
    martin.backward(20)
    martin.down()
    martin.begin_fill()
    martin.circle(5)
    martin.end_fill()
    
    turtle.done()


def draw_dog():
    # Nastavitev zaslona
    screen = turtle.Screen()
    screen.bgcolor("lightblue")

    # Ustvarjanje želve
    dog = turtle.Turtle()
    dog.color("brown")
    dog.pensize(5)

    # Nariši glavo
    dog.penup()
    dog.goto(0, -100)
    dog.pendown()
    dog.begin_fill()
    dog.circle(100)
    dog.end_fill()

    # Nariši ušesa
    dog.penup()
    dog.goto(-100, 0)
    dog.pendown()
    dog.begin_fill()
    dog.circle(40)
    dog.end_fill()

    dog.penup()
    dog.goto(100, 0)
    dog.pendown()
    dog.begin_fill()
    dog.circle(40)
    dog.end_fill()

    # Nariši oči
    dog.penup()
    dog.goto(-35, -10)
    dog.pendown()
    dog.color("black")
    dog.begin_fill()
    dog.circle(10)
    dog.end_fill()

    dog.penup()
    dog.goto(35, -10)
    dog.pendown()
    dog.begin_fill()
    dog.circle(10)
    dog.end_fill()

    # Nariši nos
    dog.penup()
    dog.goto(0, -30)
    dog.pendown()
    dog.color("pink")
    dog.begin_fill()
    dog.circle(15)
    dog.end_fill()

    # Nariši ustnice
    dog.penup()
    dog.goto(-30, -50)
    dog.pendown()
    dog.color('black')
    dog.right(90)
    dog.circle(30, 180)
    dog.hideturtle()

    # Zaključek
    turtle.done()


draw_dog()

