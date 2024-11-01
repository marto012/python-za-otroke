def naloga_1():
    sadje = ["jabolko", "kivi", "mango", "liči"]
    print(sadje)
    sadje.append("breskev")
    print(sadje)
    sadje.append("grozdje")
    print(sadje)
    sadje[2] = "ananas"
    print(sadje)
    sadje.remove("jabolko")
    print(sadje)
    del sadje[5]
    print(sadje)


def naloga_2():
    sadje = ["jabolko", "kivi", "mango", "liči"]
    print(sadje[1:3])
    print(sadje[0:4])


def naloga_3():
    sadje = ["ananas", "kaki", "mango", "liči", "breskev"]

    for element in sadje:
        print("Moje najljubše sadje je:", element, ".")


def naloga_4():
    stevilo_ucencev = [22, 24, 19, 25, 22, 23]
    i = 1

    for element in stevilo_ucencev:
        print("V", i, ". avtobusu je", element, "učencev.")
        i = i + 1


def naloga_5():
    stevila = [16, 23, 8, 2, 3, 27, 51, 32, 9, 55]
    najvecje_stevilo = 0
    
    max(stevila)
    for element in stevila:
        if element > najvecje_stevilo:
            najvecje_stevilo = element

    print('Največje število je:', najvecje_stevilo)
