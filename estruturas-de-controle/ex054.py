from datetime import date

anoAtual = date.today().year
maiorDeIdade = 0
menorDeIdade = 0

for i in range(1, 8):
    anoNascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(i)))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1

print('\nAo todo tivemos {} pessoas maiores de idade'.format(maiorDeIdade))
print('E também tivemos {} pessoas menores de idade'.format(menorDeIdade))