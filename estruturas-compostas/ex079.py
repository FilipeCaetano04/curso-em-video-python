numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if continuar in 'N':
        break

print('-=' * 20)
print(f'Você digitou os valores {sorted(numeros)}')