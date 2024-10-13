# ŽELVJA GRAFIKA IN ZANKA WHILE
from kvadrat_z_zanko_while import kvadrat_z_zanko_while
from devetkotni_in_krog import devetkotnik
from devetkotni_in_krog import krog
from kvadratna_spirala import kvadratna_spirala
from zelvja_grafika_in_zanka_while_nal import naloga_1
from zelvja_grafika_in_zanka_while_nal import naloga_2
from zelvja_grafika_in_zanka_while_nal import naloga_3
from zelvja_grafika_in_zanka_while_nal import naloga_4a
from zelvja_grafika_in_zanka_while_nal import naloga_4b
from zelvja_grafika_in_zanka_while_nal import naloga_5
from zelvja_grafika_in_zanka_while_nal import naloga_6


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. kvadrat z zanko while")
    print('2. devetkotnik ')
    print('3. krog')
    print('4. kvadratna spirala')
    print('5. naloga 1')
    print('6. naloga 2')
    print('7. naloga 3')
    print('8. naloga 4a')
    print('9. naloga 4b')
    print('10. naloga 5')
    print('11. naloga 6')

    choice = input("Vnesi število programa (1-11): ")

    if choice == "1":
        kvadrat_z_zanko_while()

    elif choice == '2':
        devetkotnik()

    elif choice == '3':
        krog()

    elif choice == '4':
        kvadratna_spirala()

    elif choice == '5':
        naloga_1()

    elif choice == '6':
        naloga_2()
 
    elif choice == '7':
        naloga_3()

    elif choice == '8':
        naloga_4a()

    elif choice == '9':
        naloga_4b()
    elif choice == '10':
        naloga_5()
    
    elif choice == '11':
        naloga_6()

    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
