# ler numero real e retornar a porção inteira

from math import trunc

# valor = float(input('Digite um número real: '))
# print()
# print('A parte inteira é: {}'.format(trunc(valor)))
# resto = valor - trunc(valor)
# print()
# print('A parte decimal é: {}'.format(resto))
# print()

# ou

valor = float(input('Digite um numero real: '))
print()
print('A parte inteira de {} é {}.'.format(valor, int(valor)))
print()
print('A parte decimal de {} é {:.2f}.'.format(valor, (valor - int(valor))))
