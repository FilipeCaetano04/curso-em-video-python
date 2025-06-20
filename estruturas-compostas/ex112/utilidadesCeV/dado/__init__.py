def leiaDinheiro(txt):
    while True:
        preco = str(input(txt)).strip().replace(',', '.')
        if preco.isnumeric():
            return float(preco)
        elif preco.count('.') == 1:
            achar_float = preco.find('.')
            inteiro = preco[:achar_float]
            flutuante = preco[achar_float + 1:]
            if inteiro.isnumeric() and flutuante.isnumeric():
                completo = inteiro + '.' + flutuante
                return float(completo)
            else:
                print(f'\033[31mERRO: \"{preco}\" não é um preço válido\033[m')
        else:
            print(f'\033[31mERRO: \"{preco}\" não é um preço válido\033[m')
