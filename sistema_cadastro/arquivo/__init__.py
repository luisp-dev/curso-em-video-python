def mostrar_pessoas(caminho):
    """Lê o arquivo de dados e exibe as pessoas cadastradas na tela."""
    with open(caminho, 'a+', encoding="utf-8") as arq:

        arq.seek(0)
        conteudo = arq.read().strip()

        if not conteudo:
            print('Nenhuma pessoa cadastrada ainda.'.center(42))
        else:
            print(conteudo)

def cadastrar_pessoa(caminho, nome, idade):
    """Grava um novo registro formatado no arquivo de texto."""
    with open(caminho, 'a+', encoding="utf-8") as arq:
        arq.write(f'{nome:<30}{idade:>7} anos' + '\n')