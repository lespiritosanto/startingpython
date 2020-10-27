# quantos litros de tinta para pintar parede, dado que cada litro pinta 2m²

CAP_TINTA = 2.0

altura = float(input('Qual a altura da parede, em metros: '))
cumprimento = float(input('Qual o cumprimento da parede, em metros: '))
area = altura * cumprimento

print('Você precisará de {} litros de tinta.'.format(area / CAP_TINTA))
