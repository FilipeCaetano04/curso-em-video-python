print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)

listagem_precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
                   'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 
                   'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for i in range(0, len(listagem_precos)):
    if i % 2 == 0:
        print(f'{listagem_precos[i]:.<30}', end = '')
    else:
        print(f'R$ {listagem_precos[i]:6.2f}')
print('-' * 40)