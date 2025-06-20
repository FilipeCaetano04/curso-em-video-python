from time import sleep
from random import randint

print('-' * 30)
print(f'{"JOGOS DE MEGA SENA":^30}')
print('-' * 30)

conjunto = []
jogos = []
N = int(input('Quantos jogos você quer que eu sorteie ? '))

for i in range(0, N):
    for j in range(0, 6):

        num = randint(1, 60)
        while num in jogos:
            num = randint(1 , 60)
        
        jogos.append(num)
    jogos.sort()
    conjunto.append(jogos[:])
    jogos.clear()

print(f'{f" SORTEANDO {N} JOGOS ":-^30}')
for i in range(0, N):
    print(f'Jogo {i + 1}: {conjunto[i]}')
    sleep(1)
