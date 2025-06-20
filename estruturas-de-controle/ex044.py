print('=' * 15 + ' LOJA PYTHON ' + '=' * 15)

valor = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opc = int(input('Qual sua opção? '))

if opc == 1:
    valorDesconto = valor * (1 - 0.1)
    print('O pagamento de R${:.2f} em dinheiro/cheque ficará R${:.2f}'.format(valor, valorDesconto))
elif opc == 2:
    valorDesconto = valor * (1 - 0.05)
    print('O pagamento de R${:.2f} á vista no cartão ficará R${:.2f}'.format(valor, valorDesconto))
elif opc == 3:
    valorParcela = valor / 2
    print('O pagamento será parcelado em 2x de R${:.2f} SEM JUROS'.format(valorParcela))
    print('O valor total será o mesmo: R${:.2f}'.format(valor))
elif opc == 4:
    parcelas = float(input('Quantas parcelas? '))
    valorJuros = valor * (1 + 0.2)
    valorParcela = valorJuros / parcelas
    print('O pagamento será parcelado em {:.0f}x de R${:.2f} COM JUROS'.format(parcelas, valorParcela))
    print('O valor da compra de R${:.2f} custará R${:.2f} no final'.format(valor, valorJuros))
else:
    print('OPÇÃO INVÁLIDA!')
 