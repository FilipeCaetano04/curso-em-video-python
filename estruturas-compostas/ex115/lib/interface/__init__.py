def leiaInt(msg):
    while True:
        try:
            numInt = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário resolveu interromper o programa!\033[m')
            break
        else:
            return numInt
        

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU DE OPÇÕES')
    for i, item in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[34m{item}\033[m')
    print(linha())

    opc = leiaInt('Sua opção: ')
    return opc