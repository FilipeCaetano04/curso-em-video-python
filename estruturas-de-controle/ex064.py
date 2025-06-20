num = int(input('Digite um número [999 para parar]: '))
totalNum = 0
soma = 0
while num != 999:
    totalNum += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles é {}'.format(totalNum, soma))
