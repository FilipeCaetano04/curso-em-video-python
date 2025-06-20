from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opc = 0

while opc != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    opc = int(input('>>>>> Qual é sua opção? '))

    if opc == 1:
        print('A soma {} + {} é {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('O produto {} x {} é {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        if num1 > num2:
            print('Entre {} e {}, o maior valor é {}'.format(num1, num2, num1))
        elif num2 > num1:
            print('Entre {} e {}, o maior valor é {}'.format(num1, num2, num2))
        else:
            print('Os dois valores são iguais')
    elif opc == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')

    print('=-=' * 12)
    sleep(2)

print('Fim do programa!')