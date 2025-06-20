conjunto = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))

    conjunto.append(pessoa.copy())
    
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo, temos {len(conjunto)} pessoas cadastradas.')
media = soma = 0
for pessoa in conjunto:
    soma += pessoa['idade']
media = soma / len(conjunto)
print(f'B) A média das idades é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end = '')
for pessoa in conjunto:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end = ' ')
print()
print('D) A lista de pessoas acima da média das idades:')
for pessoa in conjunto:
    if pessoa['idade'] > media:
        print('   ', end = '')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end = '')
        print()
print('<<< ENCERRADO >>>')