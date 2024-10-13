# ŽELVJA GRAFIKA IN ZANKA WHILE
from kvadrat_z_zanko_while import kvadrat_z_zanko_while
from devetkotni_in_krog import devetkotnik
from devetkotni_in_krog import krog
from kvadratna_spirala import kvadratna_spirala


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. kvadrat z zanko while")
    print('2. devetkotnik ')
    print('3. krog')
    print('4. kvadratna spirala')

    choice = input("Vnesi število programa (1-4): ")

    if choice == "1":
        kvadrat_z_zanko_while()

    elif choice == '2':
        devetkotnik()

    elif choice == '3':
        krog()

    elif choice == '4':
        kvadratna_spirala()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
