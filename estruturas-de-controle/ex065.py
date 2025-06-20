soma = 0
contador = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if contador == 1:
        maior = menor = num
    elif contador > 1:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
