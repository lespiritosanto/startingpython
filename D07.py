# Taboada de número inteiro

valor = int(input('Digite um número inteiro: '))
print('\033[33m=\033[m' * 30)
print('\033[30mTaboada do {}\033[m'.format(valor))
print('\033[33m=\033[m' * 30)

for i in range(1, 10):
    print('\033[30m{} x {} = {}\033[m'.format(valor, i, valor * i))
