real = float(input('Quanto dinheiro você tem na carteira? R$'))
#2016: US$ 1,00 = R$ 3,27
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))