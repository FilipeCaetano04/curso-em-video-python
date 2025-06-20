num = int(input('Digite um número: '))
contador = 0

for i in range(1, num + 1):

    if num % i == 0:
        print('\033[36m', end = '')
        contador += 1
    else:
        print('\033[m', end = '')
    print('{} '.format(i), end = '')  

print('\n\033[mO número {} foi divisível {} vezes'.format(num, contador))

if contador != 2:
    print('Por isso ele NÃO É PRIMO')
else:
    print('Por isso ele É PRIMO')
