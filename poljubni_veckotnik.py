import turtle


def poljubni_veckotnik(stevilo_stranic, velikost):
    martin = turtle.Pen()
    martin.reset()

    def veckotnik(stevilo_stranic, velikost):
        i = 1
        while i <= stevilo_stranic:
            martin.forward(velikost)
            martin.left(360 / stevilo_stranic)
            i = i + 1

    veckotnik(stevilo_stranic, velikost)

    martin.hideturtle()
