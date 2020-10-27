# aluguel de carros

DAY_PRICE = 60
KM_RODADO = 0.15

dias = int(input('Digite a quantidade de dias do aluguel do carro: '))
km = float(input('Digite a quantidade de kilômetros percorridos: '))
print('=' * 50)
print('''O valor a ser pago a título do aluguel do automóvel é de: R$ {:.2f}, 
considerando o preço diário de R$ {:.2f} e o valor por KM rodados 
de R$ {:.2f}.'''
      .format((dias * DAY_PRICE) + (km * KM_RODADO), DAY_PRICE, KM_RODADO))
