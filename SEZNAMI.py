from prvi_seznam import prvi_seznam
from funkcije_za_urejanje_seznama import funkicje_za_urejanje_seznama
from sprehodi_se_po_seznamu import sprehodi_se_po_seznamu
from seznam_10_nakljucnimi_stevili import seznam_z_10_naklucnimi_stevili
from seznami_nal import naloga_1
from seznami_nal import naloga_2
from seznami_nal import naloga_3
from seznami_nal import naloga_4
from seznami_nal import naloga_5


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. prvi seznam")
    print("2. funkcije za urejanje seznama")
    print("3. sprehodi se po seznamu")
    print("4. seznam z 10 naključnimi števili")
    print('5. naloga 1')
    print('6. naloga 2')
    print('7. naloga 3')
    print('8. naloga 4')
    print('9. naloga 5')

    choice = input("Vnesi število programa (1-9): ")

    if choice == "1":
        prvi_seznam()

    elif choice == "2":
        funkicje_za_urejanje_seznama()

    elif choice == "3":
        sprehodi_se_po_seznamu()

    elif choice == "4":
        seznam_z_10_naklucnimi_stevili()

    elif choice == '5':
        naloga_1()

    elif choice == '6':
        naloga_2()

    elif choice == '7':
        naloga_3()

    elif choice == '8':
        naloga_4()

    elif choice == '9':
        naloga_5()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
