from prvi_seznam import prvi_seznam
from funkcije_za_urejanje_seznama import funkicje_za_urejanje_seznama
from sprehodi_se_po_seznamu import sprehodi_se_po_seznamu
from seznam_10_nakljucnimi_stevili import seznam_z_10_naklucnimi_stevili


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. prvi seznam")
    print('2. funkcije za urejanje seznama')
    print('3. sprehodi se po seznamu')
    print('4. seznam z 10 naključnimi števili')

    choice = input("Vnesi število programa (1-4): ")

    if choice == "1":
        prvi_seznam()

    elif choice == '2':
        funkicje_za_urejanje_seznama()

    elif choice == '3':
        sprehodi_se_po_seznamu()

    elif choice == '4':
        seznam_z_10_naklucnimi_stevili()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
