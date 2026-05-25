def linha():
    print('-' * 42)


def cabecalho(msg):
    linha()
    print(msg.center(40))
    linha()


def mostrar_opcoes(lista):
    for i, o in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m', end=' - ')
        print(f'\033[34m{o}\033[m')
    linha()


def mostrar_menu(lista):
    cabecalho('MENU PRINCIPAL')
    mostrar_opcoes(lista)
