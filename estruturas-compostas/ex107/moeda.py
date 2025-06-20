def aumentar(preco, percent):
    precoAumento = preco * (1 + percent / 100)
    return precoAumento


def diminuir(preco, percent):
    precoDesconto = preco * (1 - percent / 100)
    return precoDesconto


def metade(preco):
    precoMetade = preco / 2
    return precoMetade


def dobro(preco):
    precoDobro = preco * 2
    return precoDobro
