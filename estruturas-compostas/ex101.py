def voto(anoNascimento):
    from datetime import date
    idade = date.today().year - anoNascimento
    situação = f'Com {idade} anos: '
    if idade < 18 and idade >= 16 or idade > 65:
        situação += 'VOTO OPCIONAL.'
    elif idade < 16:
        situação += 'Não Vota.'
    else:
        situação += 'VOTO OBRIGATÓRIO.'
    return situação


anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoNascimento))