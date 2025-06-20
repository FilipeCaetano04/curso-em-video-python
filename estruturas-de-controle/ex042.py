n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

if n1 >= n2 + n3 or n2 >= n1 + n3 or n3 >= n1 + n2:
    print('Não é possível formar um triângulo')
elif n1 == n2 and n1 == n3:
    print('É possível formar um triângulo equilátero')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('É possível formar um triângulo isósceles')
else:
    print('É possível formar um triângulo escaleno')
