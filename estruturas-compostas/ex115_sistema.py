from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = './cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sistema'])
    if resposta == 1:
        # Opção de ler o arquivo das pessoas cadastradas!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa!
        cabeçalho('NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema!
        cabeçalho('ENCERRANDO O SISTEMA')
        break
    else:
        # Opção de valor inválido!
        print('\033[31mERRO: por favor, digite um valor válido!\033[m')
    sleep(1.2)