# VEDNO TEŽJE, VEDNO BOLJ ZABAVNO; GNEZDENJE ZANK
from roza_iz_petkotnikov import roza_iz_petkotnikov
from kvadrati_v_vrsti import kvadrati_v_vrsti
from kvadrati_v_kvadratih import kvadrati_v_kvadratih
from vedno_tezje_vedno_bolj_zabavno_nal import naloga_1
from vedno_tezje_vedno_bolj_zabavno_nal import naloga_2
from vedno_tezje_vedno_bolj_zabavno_nal import naloga_3


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. roza iz petkotnikov")
    print("2. kvadrati v vrsti")
    print("3. kvadrati v kvadratih")
    print("4. naloga 1")
    print("5. naloga 2")
    print('6. naloga 3')

    choice = input("Vnesi število programa (1-6): ")

    if choice == "1":
        roza_iz_petkotnikov()

    elif choice == "2":
        kvadrati_v_vrsti()

    elif choice == "3":
        kvadrati_v_kvadratih()

    elif choice == "4":
        naloga_1()

    elif choice == "5":
        naloga_2()

    elif choice == '6':
        naloga_3()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
