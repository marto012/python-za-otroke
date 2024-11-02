from klikni import klikni
from umetniska_slika import umetniska_slika
from dolocanje_koordinat_s_spremenljivkami import dolocanje_koordinat_s_spremenkjivkami
from tkinter_grafika_in_gumbki_nal import naloga_1
from tkinter_grafika_in_gumbki_nal import naloga_2
from tkinter_grafika_in_gumbki_nal import naloga_3


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. klikni")
    print("2. umetniška slika")
    print('3. določanje koordinat s spremenljivkami')
    print('4. naloga 1')
    print('5. naloga 2')
    print('6. naloga 3')

    choice = input("Vnesi število programa (1-6): ")

    if choice == "1":
        klikni()

    elif choice == "2":
        umetniska_slika()

    elif choice == '3':
        dolocanje_koordinat_s_spremenkjivkami()

    elif choice == '4':
        naloga_1()

    elif choice == '5':
        naloga_2()

    elif choice == '6':
        naloga_3

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
