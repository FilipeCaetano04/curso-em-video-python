while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO!')