# the program must add player name, how many games he played.
# How many goals he scored in each match [list]

player = dict()
goals = []

print('-=' * 3,  'Player Performance Program',  '=-' * 3)

player['Name'] = str(input('Name of the player: ').strip().capitalize())

num = int(input(f"How many matches {player['Name']} played? "))
for i in range(0, num):
    quant = int(input(f'How many goals he scored in the {i + 1}° match? '))
    goals.append(quant)

player['Goals'] = goals[:]
player['Total goals'] = sum(goals)

print('==' * 25)
print(player)

print('==' * 25)
for k, val in player.items():
    print(f'The field {k} has the value {val}.')

print('==' * 25)
print(f"The player {player['Name']} played {num} matches.")

for index, value in enumerate(player['Goals']):
    print(f"     => In match {index + 1} he scored {value} goals.")
print(f"He scored a total of {player['Total goals']} goals.")
