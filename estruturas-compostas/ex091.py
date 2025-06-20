from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print('Valores sorteados:')
for j, n in jogadores.items():
    print(f'{j} tirou {n} no dado.')
    sleep(1)

ranking = dict(sorted(jogadores.items(), key = lambda item: item[1], reverse = True))
print('-=' * 16)
print(f'{" RANKING DOS JOGADORES ":=^33}')
cont = 1
for j, n in ranking.items():
    print(f'{cont}º lugar: {j} com {n}')
    cont += 1
