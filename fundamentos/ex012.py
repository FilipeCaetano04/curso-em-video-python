valor = float(input('Qual o valor do produto? R$'))
#desconto de 5%
valorDesconto = valor * 0.95
print('O produto que custava R${:.2f}, na promoção com um desconto de 5% custará R${:.2f}'.format(valor, valorDesconto))
