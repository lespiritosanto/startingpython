# ler velocidade do carro em km/h e dar multa se ultrapassar 80km/h
# sendo que cada km/h acima do limite custa R$ 7

VALOR_MULTA_KM = 7

vel = float(input('Digite a velocidade do veículo: '))
print()

if vel > 80:
    print('Você recebeu uma multa por ultrapassar a velocidade da via.')
    print('Valor da multa: R$ {:.2f} '.format((vel-80) * VALOR_MULTA_KM))
