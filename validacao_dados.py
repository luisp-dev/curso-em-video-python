"""Curso em Vídeo - Exercício 113: Funções Aprofundadas"""

def leia_num(tipo):
    if tipo is float:
        num_tipo = 'real'
    elif tipo is int:
        num_tipo = 'inteiro'
    while True:
        try:
            num = tipo(input(f'Digite um número {num_tipo}: '))
        except (TypeError, ValueError):
            print(f'\033[31mERRO! Digite um número {num_tipo} válido.\033[m')
        else:
            return num


inteiro = leia_num(int)
real = leia_num(float)
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
