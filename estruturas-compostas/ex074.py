from random import randint

aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1 ,10))
print('Os números gerados foram: ', end = '')
for i in range(0, 5):
    print(aleatorios[i], end = ' ')
ordem = sorted(aleatorios)
print(f'\nO maior valor sorteado foi {ordem[-1]}')
print(f'O menor valor sorteado foi {ordem[0]}')
