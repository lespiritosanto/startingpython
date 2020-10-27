# create a rock, paper and scissors game

from random import randint
import time

print('+=' * 40)
print('\033[7;30;41mYou will play rock, paper and scissors with me. Be prepared!\033[m')
print('+=' * 40)

print()
print('''The rules of the game are:
Rock beats scissors
Scissors beats paper
Paper beats rock
''')
print()

choice = 0
while choice not in range(1, 4):
    choice = int(input('''What do you choose:
    1. Rock
    2. Paper
    3. Scissors
    '''))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')

game = ['Rock', 'Paper', 'Scissors']

print()
comp_choice = randint(1, 3)

if choice == comp_choice:
    print('It tied, lets do it again. We chose {}.'.format(game[choice - 1]))
elif (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
    print('Well done! You chose {} and I chose {}. '
          '{} beats {}.'
          .format(game[choice - 1], game[comp_choice - 1],
                  game[choice - 1], game[comp_choice - 1]))
else:
    print('\033[7;30;41mHaha! You lose!\033[m I chose {} and you chose {}. '
          '{} beats {}.'
          .format(game[comp_choice - 1], game[choice - 1],
                  game[comp_choice - 1], game[choice - 1]))
