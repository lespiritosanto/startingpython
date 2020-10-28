# create a tuple that has the first 20 positions of any competition. Show the last 4,
# Show the first 5, show a list in alphabetic order and select one to show his position

soccer_teams = ('Internacional', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo',
                'Santos', 'Palmeiras', 'Fortaleza', 'Grêmio', 'Ceará SC', 'Atlético-GO',
                'Sport', 'Corinthians', 'Bahia', 'Bragantino-SP', 'Botafogo',
                'Vasco da Gama', 'Athletico-PR', 'Coritiba', 'Goiás')

while True:
    while True:
        position = int(input('Please choose a number from 1 to 20: '))
        if position in range(1, 21):
            break

    print('+=' * 30)
    print('The number you chose is the soccer team {}.'.format(soccer_teams[position - 1]))
    print('+=' * 30)

    print('The last 4 teams of the list are: {}'.format(soccer_teams[-1:-5:-1]))
    print('+=' * 30)

    print('The top 5 teams are: {}'.format(soccer_teams[0:5]))
    print('+=' * 30)

    for index, team in enumerate(soccer_teams):
        print('{}° -> {}'.format(index + 1, team))

    # way to get out of the loop
    choice = str(input('Do you want to continue? [y/n] ')).strip().casefold()[0]
    if choice[0] == 'n':
        break
