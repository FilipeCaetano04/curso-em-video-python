def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    

nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Números de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gols = gols)
else:
    ficha(nome, gols)