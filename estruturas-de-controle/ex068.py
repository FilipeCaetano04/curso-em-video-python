import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

quantVenceu = 0

while True:
    soma = 0
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    soma = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]

    print('-' * 30)
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total: {soma}, DEU PAR')
        ePar = True
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total: {soma}, DEU ÍMPAR')
        ePar = False
    print('-' * 30)
    
    if ePar:
        if escolha == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            quantVenceu += 1
        elif escolha == 'I':
            print('Você PERDEU!')
            print('=-' * 15)
            break
    else:
        if escolha == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            quantVenceu += 1
        elif escolha == 'P':
            print('Você PERDEU!')
            print('=-' * 15)
            break
    print('=-' * 30)
    
print(f'GAME OVER! Você venceu {quantVenceu} vezes.')