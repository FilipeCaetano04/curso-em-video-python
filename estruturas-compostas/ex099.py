from time import sleep

def maior(* numeros):
    print('-=' * 25)
    print('Analisando os valores passados...')
    maior = 0
    for num in numeros:
        if num > maior:
            maior = num
        print(f'{num} ', end = '', flush = True)
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 6, 7, 5, 0, 8)
maior(6, 4, 9)
maior(6, 2)
maior(10)
maior()