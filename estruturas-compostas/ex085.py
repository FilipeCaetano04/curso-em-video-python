numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('-=' * 20)

print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
