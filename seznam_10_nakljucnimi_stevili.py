import random


def seznam_z_10_naklucnimi_stevili():   
    seznam_z_nakljucnimi_stevili = []
    i = 1

    while i <= 10:
        stevilo = random.randint(1, 100)
        seznam_z_nakljucnimi_stevili.append(stevilo)
        i = i + 1

    for element in seznam_z_nakljucnimi_stevili:
        print(element)
