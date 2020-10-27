from math import hypot

# calcular hipotenusa, dado os valores dos catetos de um triangulo retangulo

c1 = float(input('Digite o valor do cateto adjacente: '))
c2 = float(input('Digite o valor do cateto oposto: '))
print()
print('A hipotenusa tem o valor de: {:.2f}.'.format(hypot(c1, c2)))
print()
