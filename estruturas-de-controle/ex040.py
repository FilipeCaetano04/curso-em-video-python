nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média é {:.1f}'.format(media))

if media < 5.0:
    print('O aluno está REPROVADO')
elif media >= 7.0:
    print('O aluno está APROVADO')
elif media < 7.0 and media >= 5.0:
    print('O aluno está de RECUPERAÇÃO')
