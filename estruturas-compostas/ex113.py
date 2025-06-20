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
        

def leiaFloat(msg):
    while True:
        try:
            numFloat = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário resolveu interromper o programa!\033[m')
            break
        else:
            return numFloat


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
    
print(f'O valor inteiro digitado foi {i} e o real foi {r}')