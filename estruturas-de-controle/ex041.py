from datetime import date

anoAtual = date.today().year
anoNasci = int(input('Ano de Nascimento: '))
idade = anoAtual - anoNasci
print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')