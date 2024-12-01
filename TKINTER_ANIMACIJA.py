from premikajoc_kvadratek import premikajoc_kvadratek
from nakljucno_premikanje_ribe import premikajoca_riba
from tkinter_animacija_nal import naloga_1
from tkinter_animacija_nal import naloga_2
from tkinter_animacija_nal import naloga_3


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. premikajoč kvadratek")
    print("2. naključno premikanje ribe")
    print("3. naloga 1")
    print("4. naloga 2")
    print("5. naloga 3")

    choice = input("Vnesi število programa (1-5): ")

    if choice == "1":
        premikajoc_kvadratek()
    elif choice == "2":
        premikajoca_riba()
    elif choice == "3":
        naloga_1()
    elif choice == "4":
        naloga_2()
    elif choice == "5":
        naloga_3()
    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()


