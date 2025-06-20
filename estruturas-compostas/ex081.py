numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = ' '

    while continuar not in 'NS':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 20)
totalElementos = len(numeros)
print(f'Você digitou {totalElementos} elementos.')
numeros.sort(reverse = True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
