from datetime import date

anoNascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Quem nasceu em {} tem ou terá {} anos em {}'.format(anoNascimento, idade, anoAtual))

if idade > 18:
    atraso = idade - 18
    anoAlist = anoAtual - atraso
    print('Você já deveria ter se alistado há {} anos'.format(atraso))
    print('Seu alistamento foi em {}'.format(anoAlist))
elif idade == 18:
    print('Você me deve se alistar no ano atual')
elif idade < 18:
    falta = 18 - idade
    anoAlist = anoAtual + falta
    print('Ainda faltam {} anos para o alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(anoAlist))
