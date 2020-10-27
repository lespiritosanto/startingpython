# ler o cumprimento de 3 retar e dizer se ele pode ou não formar um triângulo

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

s1 = r1 + r2
s2 = r1 + r3
s3 = r2 + r3

if s1 > r3 and s2 > r2 and s3 > r1:
    print('É possível construir um triângulo com as três retas.')
else:
    print('Não é possível construir um triângulo com as três retas.')
