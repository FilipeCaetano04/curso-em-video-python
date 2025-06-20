expressao = str(input('Digite uma expressão: '))
cont = 0
for i in expressao:
    if i == '(':
        cont += 1

    elif i == ')':
        cont -= 1
        if cont < 0:
            break

if cont == 0:
    print('A expressão está válida!')
else:
    print('A expressão está inválida!')


