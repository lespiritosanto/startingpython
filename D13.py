# conversor de temperaturas

temp = float(input('Digite a temperatura em °C para ser convertida: '))

f = temp * (9/5) + 32  # fórmula
k = temp + 273.15

print('A temperatura em graus Fahrenheit é de: {:.2f} °F'.format(f))
print('A temperatura em Kelvin é de: {:.2f} K'.format(k))
