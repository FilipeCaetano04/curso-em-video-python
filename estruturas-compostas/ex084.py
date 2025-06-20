pessoas = list()
dados = list()
totoalPessoas = 0
maiorPeso = 0
menorPeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    totoalPessoas += 1
    if totoalPessoas == 1:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        elif dados[1] < menorPeso:
            menorPeso = dados[1]
    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 20)
print(f'Ao todo, foram cadastrados {totoalPessoas} pessoas')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end = '')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == maiorPeso:
        print(f'[{pessoas[i][0]}] ', end = '')

print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ', end = '')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == menorPeso:
        print(f'[{pessoas[i][0]}] ', end = '')
