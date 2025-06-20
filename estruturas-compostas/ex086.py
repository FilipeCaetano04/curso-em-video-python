matriz3x3 = list()
elemento = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        elemento.append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))        
    matriz3x3.append(elemento[:])
    elemento.clear()
print('-=' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz3x3[linha][coluna]:^5}]', end = '')
    print()
