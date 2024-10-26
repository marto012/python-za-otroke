from roza_iz_kvadratov_in_barvni_kvadrati import roza_iz_kvadratov_in_barvni_kvadrati
from kvadratki_v_vrsti import kvadratki_v_vrsti
from vijuga import vijuga
from funkcije_nal import naloga_1
from funkcije_nal import naloga_2
from funkcije_nal import naloga_3
from funkcije_nal import naloga_4
from funkcije_nal import naloga_5


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. roza iz kvadratov in barvni kvadrati")
    print("2. kvadratki v vrsti")
    print('3. vijuga')
    print('4. naloga 1')
    print('5. naloga 2')
    print('6. naloga 3')
    print('7. naloga 4')
    print('8. naloga 5')

    choice = input("Vnesi število programa (1-8): ")

    if choice == "1":
        roza_iz_kvadratov_in_barvni_kvadrati()

    elif choice == "2":
        kvadratki_v_vrsti()

    elif choice == '3':
        vijuga()

    elif choice == '4':
        naloga_1()

    elif choice == '5':
        naloga_2()

    elif choice == '6':
        naloga_3

    elif choice == '7':
        naloga_4()

    elif choice == '8':
        naloga_5()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
