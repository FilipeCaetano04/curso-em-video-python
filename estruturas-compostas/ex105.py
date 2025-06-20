def notas(*notas, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando de deve ou não mostrar a situação do aluno
    :return: dicionário com várias informações sobre a situação do aluno 
    """
    dicionario = dict()
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['média'] = sum(notas) / len(notas)
    if sit == True:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else: 
            dicionario['situação'] = 'RUIM'
    return dicionario


resp = notas(5.5, 2.5, 10, 6.5, sit = True)
print(resp)