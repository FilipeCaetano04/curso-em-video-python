jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
totPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
totalGols = 0
for i in range(totPartidas):
    num = int(input(f'    Quantos gols na partida {i + 1}? '))
    totalGols += num
    jogador['gols'].append(num)
jogador['total'] = totalGols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {totPartidas} partidas.')
for i in range(totPartidas):
    print(f'  => Na partida {i + 1}, fez {jogador['gols'][i]} gols.')
print(f'Foi um total de {totalGols} gols.')