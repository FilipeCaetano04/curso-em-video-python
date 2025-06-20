velocidade = float(input('Qual a velocidade atual do veículo ? '))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade de 80Km/h !')
    print('Sua multa vai custar R${:.2f} !'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')