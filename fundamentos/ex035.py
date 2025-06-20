lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

opc = True
if lado1 >= lado2 + lado3:
    opc = False 
if lado2 >= lado1 + lado3:
    opc = False
if lado3 >= lado1 + lado2:
    opc = False

if opc:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
