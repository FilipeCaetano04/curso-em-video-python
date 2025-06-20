import math

ang = float(input('Digite um ângulo: ')) 
rad = math.radians(ang)
senAng = math.sin(rad)
cosAng = math.cos(rad)
tanAng = math.tan(rad)

print('O SENO desse ângulo vale {:.2f}'.format(senAng))
print('O COSSENO desse ângulo vale {:.2f}'.format(cosAng))
print('A TANGENTE desse ângulo vale {:.2f}'.format(tanAng))
