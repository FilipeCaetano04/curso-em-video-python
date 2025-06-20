valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
meses = anos * 12
parcelas = valorCasa / meses

print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de R${:.2f} por mês'.format(valorCasa, anos, parcelas))

if parcelas > 0.3 * salario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
