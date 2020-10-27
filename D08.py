# Conversão reais para dólar

QUOT_DOLAR = 3.27

valor = float(input('Quantos reais você tem na carteira? '))

print('Você tem o equivalente à {:2f} dólares pela quotação atual'
      .format(valor / QUOT_DOLAR))
