numeros = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
       for j in range(0, tamanho):
            if num <= numeros[j]:
                numeros.insert(j, num)
                print(f'Adicionado na posição {j} da lsita...')
                break
            if j == (tamanho - 1):
                numeros.append(num)
                print('Adicionado ao final da lista...')
    tamanho = len(numeros)
print(numeros)

