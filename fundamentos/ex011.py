largura = float(input('Forneça a largura da parede em metros: '))
altura = float(input('Forneça a altura da parede em metros: '))
area = largura * altura
#1l de tinta para 2m²
litros = area / 2
print('Para pintar {}m² da parede, será necessário {} litros de tinta.'.format(area, litros))
