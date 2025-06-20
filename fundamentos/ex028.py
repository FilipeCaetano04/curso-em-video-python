import random

aleatorio = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
escolha = int(input('Em qual número pensei? '))

if aleatorio == escolha:
    print('Parabéns, você acertou!')
else:
    print('Você errou! :(')
    print('Eu pensei no número {} e não no {}!'.format(aleatorio, escolha))
