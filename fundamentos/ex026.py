frase = str(input('Digite uma frase: ')).strip()

print('A letra "A" aparece {} vez(es)'.format(frase.upper().count('A')))
print('A primeira posição que ela aparece é {}'.format(frase.upper().find('A') + 1))
print('A última posição que ela aparece é {}'.format(frase.upper().rfind('A') + 1))