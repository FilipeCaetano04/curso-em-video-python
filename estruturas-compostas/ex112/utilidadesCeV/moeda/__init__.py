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
    formatado = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatado


def resumo(preco=0, perAumento=0, perDesconto=0):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Metade do preço:\t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{perAumento}% de aumento: \t{aumentar(preco, perAumento, True)}')
    print(f'{perDesconto}% de desconto:\t{diminuir(preco, perDesconto, True)}')