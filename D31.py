# pegar distancia de viagem em km. Calcular preço da passagem, sendo que cada
# km custa R$ 0,5 até 200km e R$ 0,45 para viagens mais longas

VIAGEM_CURTA = 0.5
VIAGEM_LONGA = 0.45

distancia = float(input('Digite a distancia em KM até o lugar desejado: '))

if distancia > 200:
    print('O valor da passagem é de R$ {:.2f}.'.format(distancia * VIAGEM_LONGA))
else:
    print('O valor da passagem é de R$ {:.2f}.'.format(distancia * VIAGEM_CURTA))
