# make D93 better by adding multiple players and a system to check the players details

player = dict()
team = []
goals = []

print('-=' * 3,  'Player Performance Program',  '=-' * 3)

while True:
    player['Name'] = str(input('Name of the player: ').strip().capitalize())

    num = int(input(f"How many matches {player['Name']} played? "))
    for i in range(0, num):
        quant = int(input(f'How many goals he scored in the {i + 1}° match? '))
        goals.append(quant)

    player['Goals'] = goals[:]
    player['Total goals'] = sum(goals)

    print(f"The player {player['Name']} played {num} matches.")
    print('==' * 25)

    team.append(player.copy())
    player.clear()
    goals.clear()

    choice = str(input('Do you want to continue? [y/n] ').strip().casefold()[0])
    while choice not in 'ny':
        choice = str(input('Do you want to continue? [y/n] ').strip().casefold()[0])

    if choice == 'n':
        break

print('==' * 25)
print('Cod', end=' ')
for i in team[0].keys():
    print(f'{i:<13}', end='')
print()
print('-' * 35)

for k, val in enumerate(team):
    print(f'{k+1:>2} ', end='')
    for d in val.values():
        print(f'{str(d):<13}', end='')
    print()
print('-' * 35)

while True:
    data = int(input('Show data of which player? [0 to end] '))
    if data == 0:
        break

    while data not in range(1, len(team) + 1):
        data = int(input('Show data of which player? [0 to end] '))

    print(f"  == Data of {team[data - 1]['Name']}:")
    for i in range(0, len(team[data - 1]['Goals'])):
        print(f"In the {i+1}° game {team[data - 1]['Name']} scored {team[data - 1]['Goals'][i]} goals.")
    data = 0
    print('-' * 35)

print('=>', 'Please come again', '<=')
