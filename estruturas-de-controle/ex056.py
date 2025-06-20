media = 0
quantMulher = 0
idadeMaior = 0

for i in range(1, 5):
    print('-' * 5 + ' {}º PESSOA '.format(i) + '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade / 4
    
    if sexo == 'M':
        if idade > idadeMaior:
            idadeMaior = idade
            nomeDoMaisVelho = nome
    
    if sexo == 'F':
        if idade < 20:
            quantMulher += 1

print('\nA média da idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} ano e se chama {}'.format(idadeMaior, nomeDoMaisVelho))
print('Ao todo, {} mulheres tem menos de 20 anos'.format(quantMulher))
