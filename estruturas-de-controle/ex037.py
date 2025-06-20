num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCATAL
[3] Converter para HEXADECIMAL''')
opc = int(input('Sua opção: '))

if opc == 1:
    print('O número {} na base binária é {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O número {} na base octal é {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O número {} na base hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
