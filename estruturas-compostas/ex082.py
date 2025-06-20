completa = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    completa.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 20)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')