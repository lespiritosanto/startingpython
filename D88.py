# create a program that simulates a mega sena. The program must ask
# how many games the user wants to generate. It will create 6 numbers
# between 1 and 60 for each game, putting all in a compost list

from random import randint

n = int(input('How many games do you want to generate? '))
games = []

for i in range(0, n):
    temp = []
    for sort in range(0, 6):
        temp.append(randint(1, 60))

    games.append(temp[:])
    temp.clear()

print('+=' * 20)
print('The games are: ')
for i in games:
    print(i)
