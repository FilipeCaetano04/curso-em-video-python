tupla = ('zero', 'um', 'dois', 'três', 'quatro', 
         'cinco', 'seis', 'sete', 'oito', 'nove', 
         'dez', 'onze', 'doze', 'treze', 'quatorze', 
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 
         'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num not in range(0, 21):
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {tupla[num]}')