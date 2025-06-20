numeros = []
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=' * 40)
print(f'Você digitou os valores {numeros}')

print(f'O maior valor digitado foi {max(numeros)} nas posições ', end = '')
for p, i in enumerate(numeros):
    if max(numeros) == i:
        print(p, end = '... ')

print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end = '')
for p, i in enumerate(numeros):
    if min(numeros) == i:
        print(p, end = '... ')