peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura ** 2

print('O IMC desse pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Atenção, Você está ABAIXO do peso ideal')
elif imc < 25:
    print('Parabéns, Você esta no peso IDEAL')
elif imc < 30:
    print('Atenção, Você está com SOBREPESO')
elif imc < 40:
    print('Atenção, Você está com OBESIDADE')
elif imc >= 40:
    print('Cuidado, Você está com OBESIDADE MÓRBIDA')
