from time import sleep
from random import randint

def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end = '')
    for i in range(0, 5):
       lista.append(randint(0, 10)) 
       print(f'{lista[i]} ', end = '', flush = True)
       sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Soamndo os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)