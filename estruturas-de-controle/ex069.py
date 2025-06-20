maior18 = 0
quantHomens = 0
quantMulheresMenor20 = 0

while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UM PESSOA'))
    print('-' *30 )

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' *30)

    if idade > 18:
        maior18 += 1
    
    if sexo == 'M':
        quantHomens += 1
    elif sexo == 'F':
        if idade < 20:
            quantMulheresMenor20 += 1

    continuar = ' '
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {quantHomens} homens cadastrados')
print(f'E temos {quantMulheresMenor20} mulheres com menos de 20 anos')