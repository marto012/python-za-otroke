from roza_iz_kvadratov_in_barvni_kvadrati import roza_iz_kvadratov_in_barvni_kvadrati
from kvadratki_v_vrsti import kvadratki_v_vrsti
from vijuga import vijuga
from funkcije_nal import naloga_1
from funkcije_nal import naloga_2


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. roza iz kvadratov in barvni kvadrati")
    print("2. kvadratki v vrsti")
    print('3. vijuga')
    print('4. naloga 1')
    print('5. naloga 2')

    choice = input("Vnesi število programa (1-5): ")

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

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
