numeros = (int(input('Digite um número: ')), 
           int(input('Digite outro número: ')), 
           int(input('Digite mais um número: ')), 
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')