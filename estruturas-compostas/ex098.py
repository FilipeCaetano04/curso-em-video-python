from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p = -(p)
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        for j in range(i, f + 1, p):
            print(f'{j} ', end = '', flush = True)
            sleep(0.5)
        print('FIM!')
    elif i > f:
        for j in range(i, f - 1, -(p)):
            print(f'{j} ', end = '', flush = True)
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
