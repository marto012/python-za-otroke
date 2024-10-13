# ŽELVJA GRAFIKA IN ZANKA WHILE
from kvadrat_z_zanko_while import kvadrat_z_zanko_while


def main():
    print("Izberi program, ki ga želiš izvesti:")
    print("1. vagon")
    
    choice = input("Vnesi število programa (1-1): ")

    if choice == "1":
        kvadrat_z_zanko_while()
    else:
        print("Neveljavna izbira!")


if __name__ == "__main__":
    main()
