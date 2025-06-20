print('-' * 30)
print('{:^30}'.format('LOJA SUPER EM CONTA'))
print('-' * 30)

valorTotal = 0
precoMaisDe1000 = 0
contador = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    valorTotal += preco
    contador += 1

    if contador == 1:
        menorPreco = preco
        nomeMenorPreco = nome
    else:
        if preco < menorPreco:
            menorPreco = preco
            nomeMenorPreco = nome
    
    if preco > 1000:
        precoMaisDe1000 += 1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        
    if continuar == 'N':
        break

print('{:-^30}'.format('FIM DO PROGRAMA'))
print('O total da compra foi R${:.2f}'.format(valorTotal))
print('Temos {} produtos custando mais que R$1000.00'.format(precoMaisDe1000))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nomeMenorPreco, menorPreco))
