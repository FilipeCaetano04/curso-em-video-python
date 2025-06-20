num = int(input('Digite um número para calcular seu fatorial: '))
i = num
fatorial = 1
print('{}! = '.format(num), end = '')
while i > 0:
    fatorial *= i
    print(i, end = '')
    if i > 1:
        print(' x ', end = '')
    else:
        print(' = ', end = '')
    i -= 1
print('{}'.format(fatorial))
