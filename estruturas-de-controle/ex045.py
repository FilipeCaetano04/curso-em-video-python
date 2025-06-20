from time import sleep
from random import randint 

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual sua opção? '))
computador = randint(0, 2)
opçoes = ['PEDRA', 'PAPEL', 'TESOURA']


print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA !!!')


print('\nJogador escolheu {}'.format(opçoes[jogador]))
print('Computador escolheu {}\n'.format(opçoes[computador]))

if jogador == 0 and computador == 1:
    print('COMPUTADOR VENCEU')
elif jogador == 0 and computador == 2:
    print('JOGADOR VENCEU')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCEU')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCEU')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR VENCEU')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCEU')
elif jogador == computador:
    print('EMPATE')
