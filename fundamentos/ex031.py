km = float(input('Qual a distância da sua viagem? '))

if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50

print('Sua viagem de {}Km está prestes a começar.'.format(km))
print('E o preço da sua passagem é R${:.2f}'.format(preco))
