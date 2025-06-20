frase = str(input('Digite uma frase: ')).strip().upper()
fraseLista = frase.split()
fraseJunta = ''.join(fraseLista)
fraseInversa = fraseJunta[::-1] 

''' 
Maneira alternativa:
fraseInversa = ''
for i in range(len(fraseJunta) - 1, -1, -1):
    fraseInversa += fraseJunta[i]
'''

print('O inverso de {} é {}'.format(fraseJunta, fraseInversa))

if fraseJunta == fraseInversa:
    print('É Palíndromo!')
else:
    print('Não é Palíndromo!')
