conjunto = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    totalGols = 0
    for i in range(partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))
        totalGols += jogador['gols'][i]

    jogador['total'] = totalGols
    conjunto.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":>3}')
print('-' * 60)
for i in range(len(conjunto)):
    print(f'{i:<5}{conjunto[i]['nome']:<15}{str(conjunto[i]['gols']):<15}{conjunto[i]['total']:>3}')
print('-' * 60)
while True:
    num = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if num == 999:
        break
    elif num not in range(len(conjunto)):
        print(f'ERRO! Não existe jogador com código {num}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {conjunto[num]['nome'].upper()}:')
        for i, g in enumerate(conjunto[num]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 60)
print('<<< ENCERRADO >>>')