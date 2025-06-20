print('=' * 30 + '\n{:^30}\n'.format('10  TERMOS DE UMA PA') + '=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
i = 0

while i < 10:
    print('{}'.format(termo), end = ' → ')
    termo += razao
    i += 1
print('FIM')
