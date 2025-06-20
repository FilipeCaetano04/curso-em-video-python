print('-' * 30)
print('{:^30}'.format('Sequência de Fibonacci'))
print('-' * 30)

i = int(input('Quantos termos você quer mostrar? '))

primeiro = 0
segundo = 1
termo = 1
while i > 0:
    print('{} → '.format(termo), end = '')
    termo = primeiro + segundo
    primeiro = segundo
    segundo = termo
    i -= 1
print('FIM')
