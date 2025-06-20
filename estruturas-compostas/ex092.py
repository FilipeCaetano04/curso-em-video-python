from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = 2018 - anoNascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] > 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - anoNascimento
print('-=' * 15)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}')