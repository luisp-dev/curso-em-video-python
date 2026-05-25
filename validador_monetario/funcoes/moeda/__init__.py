def metade(valor, formato=False):
    '''
    Calcula a metade de um valor, com formatação opcional.
    :param valor: o preço numérico a ser calculado
    :param formato: (opcional) indica se deve ou não formatar o valor
    :return: valor dividido pela metade
    '''
    result = valor / 2
    return result if formato is False else formatar(result)


def dobro(valor, formato=False):
    '''
    Calcula o dobro de um valor, com formatação opcional.
    :param valor: o preço numérico a ser calculado
    :param formato: (opcional) indica se deve ou não formatar o valor
    :return: valor dobrado
    '''
    result = valor * 2
    return result if formato is False else formatar(result)


def aumento(valor, taxa_aum=10, formato=False):
    '''
    Calcula o aumento percentual de um valor, com formatação opcional.
    :param valor: o preço numérico inicial
    :param taxa_aum: porcentagem de aumento
    :param formato: (opcional) indica se deve ou não formatar o valor
    :return: valor aumentado percentualmente
    '''
    result = valor + valor * taxa_aum / 100
    return result if formato is False else formatar(result)


def reducao(valor, taxa_red=10, formato=False):
    '''
    Calcula a redução percentual de um valor, com formatação opcional.
    :param valor: o preço numérico inicial
    :param taxa_red: porcentagem de redução
    :param formato: (opcional) indica se deve ou não formatar o valor
    :return: valor reduzido percentualmente
    '''
    result = valor - valor * taxa_red / 100
    return result if formato is False else formatar(result)


def formatar(valor):
    '''
    Formata o valor incluindo "R$" e trocando "." por ","
    :param valor: o preço numérico a ser formatado.
    :return: valor formatado
    '''
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor, taxa_aum=10, taxa_red=10):
    '''
    Gera uma tabela tabulada com o resumo de todas as operações monetárias.
    :param valor: o preço numérico a ser usado como argumento.
    :param taxa_aum: porcentagem de aumento
    :param taxa_red: porcentagem de redução
    '''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{'Preço analisado:':<20}{formatar(valor):>10}')
    print(f'{'Dobro do preço:':<20}{dobro(valor, True):>10}')
    print(f'{'Metade do preço:':<20}{metade(valor, True):>10}')
    print(f'{f"{taxa_aum}% de aumento:":<20}{aumento(valor, taxa_aum, True):>10}')
    print(f'{f"{taxa_red}% de redução:":<20}{reducao(valor, taxa_red, True):>10}')
    print('-' * 30)
