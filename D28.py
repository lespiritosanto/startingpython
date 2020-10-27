# gerar numero de 0 a 5 e usuario acertar o numero
# se a pessoa errar, o computador vence

from random import randint
from time import sleep

bingo = randint(0, 5)

escolha = int(input('Digite um número entre 0 e 5 '))

print()
print('Processando...')
sleep(2)

if escolha != bingo:
    print('O Computador venceu. O numero sorteado era: {}'
          .format(bingo))
else:
    print('Parabéns, você acertou o número')
