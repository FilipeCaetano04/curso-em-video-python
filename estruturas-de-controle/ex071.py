print('=' * 30)
print('BANCO CEV'.center(30))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
cedula50 = valor // 50
valor = valor % 50
cedula20 = valor // 20
valor = valor % 20
cedula10 = valor // 10
cedula1 = valor % 10

if cedula50 > 0:
    print(f'Total de {cedula50} cédulas de R$50')
if cedula20 > 0:
    print(f'Total de {cedula20} cédulas de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao Banco CEV!')

'''
total = int(input('Que Valor você quer sacar ? R$'))
ced = 50 
totalCed = 0

while True:
    
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Totla de {totalCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV!')
'''
