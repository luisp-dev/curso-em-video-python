"""Curso em Vídeo - Exercício 115: Criando Menu"""

from interface import menu
from pathlib import Path
from arquivo import mostrar_pessoas, cadastrar_pessoa

opcoes = [
    'Ver pessoas cadastradas',
    'Cadastrar nova Pessoa',
    'Sair do Sistema'
]

caminho = Path(__file__).parent / "arquivo" / "arquivo.txt"

if __name__ == '__main__':
    while True:
        menu.mostrar_menu(opcoes)
        opcao = input('\033[33mSua Opção: \033[m').strip()

        if opcao == '1':
            menu.cabecalho('PESSOAS CADASTRADAS')
            mostrar_pessoas(caminho)

        elif opcao == '2':
            menu.cabecalho('NOVO CADASTRO')
            nome = input('Nome: ')
            if not nome:
                nome = 'Desconhecido'

            while True:
                try:
                    idade = int(input('Idade: '))
                    break
                except ValueError:
                    print('\033[31mERRO! Digite uma idade válida.\033[m')

            cadastrar_pessoa(caminho, nome, idade)

        elif opcao == '3':
            menu.cabecalho('Saindo do Sistema... Até logo')
            break

        else:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
