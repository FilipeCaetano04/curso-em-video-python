nome = str(input('Digite um nome: ')).strip()
primeiro = nome.split()[0]
ultimo = nome.split()[-1]

print('O primeiro nome é {}'.format(primeiro))
print('O último nome é {}'.format(ultimo))