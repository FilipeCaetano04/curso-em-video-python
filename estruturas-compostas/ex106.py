c = ('\033[0;0m',      # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;37;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
    );


def título(txt, cor = 0):
    tam = len(txt) + 4
    print(c[cor], end = '')
    print('~' * tam)
    print(f'  {txt}  ')
    print('~' * tam)
    print(c[0], end = '')


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'')
    #print(c[6], end = '')
    print(help(com))
    #print(c[0], end = '')


while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!')
