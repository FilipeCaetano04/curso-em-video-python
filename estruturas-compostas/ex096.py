def area(l, c):
    area = l * c
    print(f'A área de um terreno {l}m x {c}m é {area}m²')


print('Controle de Terreno')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
