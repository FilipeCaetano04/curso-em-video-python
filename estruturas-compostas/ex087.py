matriz3x3 = []
elemento = []
somaPares = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0
for i in range(0, 3):
    for j in range(0, 3):
        elemento.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if elemento[j] % 2 == 0:
            somaPares += elemento[j]
    matriz3x3.append(elemento[:])
    elemento.clear()
print('-=' * 15)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz3x3[i][j]:^5}]', end = '')

    somaTerceiraColuna += matriz3x3[i][2]
    if i == 0:
        maiorSegundaLinha = matriz3x3[1][i]
    elif matriz3x3[1][i] > maiorSegundaLinha:
        maiorSegundaLinha = matriz3x3[1][i]
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}')