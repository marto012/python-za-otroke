def vsota():
    print("vsota prvih petih naravnil števil je:", 1 + 2 + 3 + 4 + 5)


def ploscina_kvadrata(a):
    print("ploscina kvadrata s stranico", a, "je:", a * a)


def obseg_pravokotnika(a, b):
    def obseg_pravokotnika_2(a, b):
        obseg = 2 * a + 2 * b
        return obseg

    dolzina_zice = obseg_pravokotnika_2(a, b)
    print('Dolzina žice za ograjo mara biti dolga', dolzina_zice, 'metrov.')


def vecje_stevilo(a, b):
    def vecje_stevilo_2(a, b):
        if a > b:
            return True
        
    if vecje_stevilo_2(a, b):
        print('Prvo število je večje od drugega.')

    else:
        print('Prvo število ni večje od drugega.')
