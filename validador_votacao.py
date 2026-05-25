"""Curso em Vídeo - Exercício 101: Funções para Votação"""

def pode_votar(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        situacao = 'VOTO NEGADO'
    elif idade < 18 or idade > 65:
        situacao = 'VOTO OPCIONAL'
    else:
        situacao = 'VOTO OBRIGATÓRIO'

    return idade, situacao


ano_nasc = int(input('Em que ano você nasceu? '))
idade_usuario, status_voto = pode_votar(ano_nasc)
print(f'Com {idade_usuario} anos: {status_voto}')
