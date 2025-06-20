times = ('Palmeiras', 'Grêmio', 'Atlético Mineiro', 'Flamengo',
         'Botafogo', 'Red Bull Bragantino', 'Fluminense', 'Atlético Paranaense',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá Esporte Clube', 'Corinthians',
         'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')

for i in range(1, 6):
    print('=' * 35)
    if i == 1:
        print(f'Lista de Times do Brasileirão 2023: {times}')
    elif i == 2:
        print(f'Os 5 primeiros são {times[:5]}')
    elif i == 3:
        print(f'Os 4 últimos são {times[-4:]}')
    elif i == 4:
        print(f'Times em ordem alfabética: {sorted(times)}')
    elif i == 5:
        posição = times.index('Fortaleza') + 1
        print(f'O Fortleza está na {posição}° posição\n')
