from random import randint

computador = randint(0, 10)

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Você consegue adivinhar qual foi?''')

jogador = int(input('Qual o seu palpite? '))
tentativa = 1

while computador != jogador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual o seu palpite? '))
    tentativa += 1

print('Você acertou com {} tentativas!'.format(tentativa))