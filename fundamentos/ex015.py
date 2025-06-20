dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
#R$60 por dia, R$0,15 por km
valor = (60 * dias) + (0.15 * km)
print('O total a pagar é R${:.2f}'.format(valor))
