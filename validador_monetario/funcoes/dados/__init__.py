def leia_dinheiro(msg):
    while True:
        try:
            valor = input(msg).strip().replace(',', '.')
            return float(valor)
        except ValueError:
            print(f'\033[31mERRO:"{valor}" é um preço inválido!\033[m')
