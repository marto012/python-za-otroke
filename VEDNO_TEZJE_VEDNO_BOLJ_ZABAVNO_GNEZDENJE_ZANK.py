# VEDNO TEŽJE, VEDNO BOLJ ZABAVNO; GNEZDENJE ZANK
from roza_iz_petkotnikov import roza_iz_petkotnikov
from kvadrati_v_vrsti import kvadrati_v_vrsti
from kvadrati_v_kvadratih import kvadrati_v_kvadratih


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. roza iz petkotnikov")
    print('2. kvadrati v vrsti')
    print('3. kvadrati v kvadratih')

    choice = input("Vnesi število programa (1-3): ")

    if choice == "1":
        roza_iz_petkotnikov()

    elif choice == '2':
        kvadrati_v_vrsti()

    elif choice == '3':
        kvadrati_v_kvadratih()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
