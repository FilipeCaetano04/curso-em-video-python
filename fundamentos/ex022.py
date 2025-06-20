nome = str(input('Digite seu nome completo: ')).strip()
print('Com letras maúsculas: {}'.format(nome.upper()))
print('Com letras minúsculas: {}'.format(nome.lower()))

nomeJunto = ''.join(nome.split())
print('O nome sem espaços possui {} letras'.format(len(nomeJunto)))

print('O primeiro nome tem {} letras'.format(len(nome.split()[0])))