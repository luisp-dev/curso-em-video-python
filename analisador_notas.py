"""Curso em Vídeo - Exercício 105: Analisando e Gerando Dicionários"""

def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n) / len(n),
    }
    if sit:
        if dados['media'] < 5:
            situacao = 'RUIM'
        elif dados['media'] < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        dados['situacao'] = situacao
    return dados


resp = notas(5.5, 8.2, 7, 4, sit=True)
print(resp)
help(notas)
