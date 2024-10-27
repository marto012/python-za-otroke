import turtle

from kvadrat_poljubne_velikosti import kvadrat_poljubne_velikosti
from pet_kvadratov_poljubne_velikosti import pet_kvadratov_poljubne_velikosti
from poljubni_veckotnik import poljubni_veckotnik
from zgledi_s_funkcijami import vsota
from zgledi_s_funkcijami import ploscina_kvadrata
from zgledi_s_funkcijami import obseg_pravokotnika
from zgledi_s_funkcijami import vecje_stevilo
from funkcije_z_vhodnimi_podatki_nal import naloga_1
from funkcije_z_vhodnimi_podatki_nal import naloga_2
from funkcije_z_vhodnimi_podatki_nal import naloga_3


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. kvadrat poljubne velikosti")
    print("2. pet kvadratov poljubne velikosti")
    print("3. veckotnik_s_poljubnim_stevilom_stranic_in_poljubno_dolzino_stranice")
    print("4. vsota prvih petih naravnih števil")
    print("5. ploščina kvadrata")
    print("6. obseg pravokotnika")
    print("7. večje število")
    print("8. naloga 1")
    print("9. naloga 2")
    print('10. naloga 3')

    choice = input("Vnesi število programa (1-10): ")

    if choice == "1":
        kvadrat_poljubne_velikosti(50)

    elif choice == "2":
        pet_kvadratov_poljubne_velikosti(20)

    elif choice == "3":
        poljubni_veckotnik(3, 30)
        poljubni_veckotnik(4, 50)
        poljubni_veckotnik(5, 70)
        turtle.done()

    elif choice == "4":
        vsota()

    elif choice == "5":
        ploscina_kvadrata(10)

    elif choice == "6":
        obseg_pravokotnika(30, 40)

    elif choice == "7":
        vecje_stevilo(10, 7)

    elif choice == "8":
        naloga_1(30)
        naloga_1(50)
        naloga_1(35)
        turtle.done()

    elif choice == "9":
        naloga_2(20)

    elif choice == '10':
        naloga_3(7)

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
