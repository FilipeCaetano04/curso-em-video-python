def aumentar(preco=0, percent=0, format = False):
    precoAumento = preco * (1 + percent / 100)
    if format:
        return moeda(precoAumento)
    else:
        return precoAumento


def diminuir(preco=0, percent=0, format = False):
    precoDesconto = preco * (1 - percent / 100)
    if format:
        return moeda(precoDesconto)
    else:
        return precoDesconto


def metade(preco=0, format = False):
    precoMetade = preco / 2
    if format:
        return moeda(precoMetade)
    else:
        return precoMetade
    

def dobro(preco=0, format = False):
    precoDobro = preco * 2
    if format:
        return moeda(precoDobro)
    else:
        return precoDobro


def moeda(preco=0, moeda = 'R$'):
    formatado = f'{moeda}{preco:>.2f}'
    return formatado