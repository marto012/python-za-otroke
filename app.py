# RISANJE Z ŽELVO-ŽELVJA GRAFIKA
from vagon import vagon
from pravokotnik import pravokotnik
from barvne_crte import barvne_crte
from risanje_po_koordinatah import risanje_po_koordinatah
from risanje_z_zelvo_zelvja_grafika_nal import naloga_1
from risanje_z_zelvo_zelvja_grafika_nal import naloga_2
from risanje_z_zelvo_zelvja_grafika_nal import naloga_3


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. vagon")
    print("2. pravokotnik")
    print("3. barvne črte")
    print("4. risanje po koordinatah")
    print("5. naloga 1")
    print("6. naloga 2")
    print('7. naloga 3')

    choice = input("Vnesi število programa (1-7): ")

    if choice == "1":
        vagon()
    elif choice == "2":
        pravokotnik()
    elif choice == "3":
        barvne_crte()
    elif choice == "4":
        risanje_po_koordinatah()
    elif choice == "5":
        naloga_1()
    elif choice == "6":
        naloga_2()
    elif choice == "7":
        naloga_3()
    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()


# martin.forward(100)
# 1. primer
# pravokotnik()
# 2. primer
# barvne_crte()
# 3. primer
# vagon()
# 4. primer
# risanje_po_koordinatah()
# naloge
# 1.
# naloga_1()
# 2.
# naloga_2()
# 3.
# naloga_3()
