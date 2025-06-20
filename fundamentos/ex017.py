import math 

c_oposto = float(input('Comprimento do cateto oposto: '))
c_adj = float(input('Comprimento do cateto adjacente: '))
''' Forma alternativa: hipotenusa = math.sqrt((c_oposto ** 2 + c_adj ** 2)) '''
hipotenusa = math.hypot(c_oposto, c_adj)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
