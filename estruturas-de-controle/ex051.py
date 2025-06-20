print('=' * 30 + '\n{:^30}\n'.format('10 TERMOS DE UMAM PA') + '=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(1, 11):
    print(termo , end = ' → ')
    termo += razao

print('ACABOU')
