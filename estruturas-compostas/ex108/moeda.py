def aumentar(preco=0, percent=0):
    precoAumento = preco * (1 + percent / 100)
    return precoAumento


def diminuir(preco=0, percent=0):
    precoDesconto = preco * (1 - percent / 100)
    return precoDesconto


def metade(preco=0):
    precoMetade = preco / 2
    return precoMetade


def dobro(preco=0):
    precoDobro = preco * 2
    return precoDobro

def moeda(preco=0, moeda = 'R$'):
    formatado = f'{moeda}{preco:>.2f}'
    return formatado