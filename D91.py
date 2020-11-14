# create a program where 4 players throw a dice (D6) and put the data in a dict.
# Put the dict in order and show who is the winner

from random import randint
from time import sleep
from operator import itemgetter

dice = dict()
ranking = dict()

for i in range(0, 4):
    dice[f'Player {i + 1}'] = randint(1, 6)

print('Sorted values: ')
for item, value in dice.items():
    sleep(1)
    print(f'{item} threw {value}.')

ranking = sorted(dice.items(), key=itemgetter(1), reverse=True)

print('-=' * 25)
print('=' * 3, 'Player Ranking', '=' * 3)
counter = 1
for i, k in ranking:
    sleep(1)
    print(f'{counter}° place is {i} with {k} points.')
    counter += 1
