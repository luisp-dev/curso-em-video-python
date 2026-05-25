"""Curso em Vídeo - Exercício 095: Aprimorando os Dicionários"""

time = []

while True:
    jogador = {'nome': input('Nome do Jogador: ')}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = [
        int(input(f'    Quantos gols na partida {p + 1}? '))
        for p in range(partidas)
    ]
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
        if continuar not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 25)
print(f'{"cod":>3} {"nome":<20}{"gols":<20}{"total":<5}')
print('-' * 50)
for i, j in enumerate(time):
    print(f'{i:>3} {j["nome"]:<20}{str(j["gols"]):<20}{j["total"]:<5}')
print('-' * 50)

while True:
    selecionar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if selecionar == 999:
        break
    if selecionar < 0 or selecionar >= len(time):
        print(f'ERRO! Não existe jogador com código {selecionar}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[selecionar]["nome"]}:')
        for i, j in enumerate(time[selecionar]['gols']):
            print(f'    No jogo {i+1} fez {j} gols.')
        print('-' * 50)

print('<< VOLTE SEMPRE >>')
