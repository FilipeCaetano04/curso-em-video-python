n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 >= n3:
        menor = n3
    else:
        menor = n2
else:
    if n2 >= n1 and n2 >= n3:
        maior = n2
        if n1 >= n3:
            menor = n3
        else:
            menor = n1
    else:
        if n3 >= n1 and n3 >= n2:
            maior = n3
            if n1 >= n2:
                menor = n2
            else:
                menor = n1

print('\nO maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
