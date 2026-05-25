"""Curso em Vídeo - Exercício 084: Lista Composta e Análise de Dados"""

pessoas = []
maior_peso = menor_peso = 0

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    if len(pessoas) == 0:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

    pessoas.append([nome, peso])

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('-' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior_peso:.2f}Kg. Peso de ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
        
print(f'\nO menor peso foi de {menor_peso:.2f}Kg. Peso de ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
