import turtle


def draw_polygon(sides):
    """Nariši enakostranični poligon z danim številom strani."""
    pen = turtle.Pen()
    angle = 360 / sides  # Izračunaj notranji kot

    for _ in range(sides):
        pen.forward(50)  # Dolžina stranice
        pen.left(angle)  # Obrni se za izračunan kot

    pen.hideturtle()


def main():
    # Vprašaj uporabnika za število kotnikov
    num_polygons = int(input("Kolikokotnik želiš narisarti (minimalno 3 kotnik): "))

    # Ustvari nov Turtle zaslon
    screen = turtle.Screen()
    screen.title("Risanje kotnikov ")

    # Preveri, ali je število strani vsaj 3
    while num_polygons < 3:
        print("Število strani mora biti vsaj 3.")
        num_polygons = int(input("Vnesite ponovno: "))

    for i in range(1):
        draw_polygon(num_polygons)  # Risanje poligona
    
    turtle.done()


main()
