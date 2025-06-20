palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in range(0, len(palavras)):
    print(f'Na palavra {palavras[i].upper()} temos ', end = '')
    for letra in palavras[i]:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
    print()