print('Digite 6 números inteiros:')

soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(i)))
    if num % 2 == 0:
        soma += num
        
print('A soma dos números pares fornecidos é {}'.format(soma))