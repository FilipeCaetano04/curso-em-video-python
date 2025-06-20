from time import sleep

conjunto_alunos = list()
aluno = list()
notas = list()
totalAlunos = 0

while True:
    soma = 0
    media = 0
    nome = str(input('Nome: '))
    for i in range(0, 2):
        nota = float(input(f'Nota {i + 1}: '))
        soma += nota
        notas.append(nota)

    aluno.append(nome)
    aluno.append(notas[:])
    media = soma / 2
    aluno.append(media)
    conjunto_alunos.append(aluno[:])
    notas.clear()
    aluno.clear()

    continua = ' '
    while continua not in 'NS':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break

print('-=' * 15)
print('Nº  NOME          MÉDIA')
print('-' * 30)
for i in range(0, len(conjunto_alunos)):
    print(f'{i}   {conjunto_alunos[i][0]:10}    {conjunto_alunos[i][2]:5}')
print('-' * 30)

while True:
    num = int(input('Mostrar a nota de qual aluno? (999 para parar): '))
    if num == 999:
        break
    elif num in range(len(conjunto_alunos)):
        print(f'Notas de {conjunto_alunos[num][0]} são {conjunto_alunos[num][1]}')
    print('-' * 30)
    
    
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')