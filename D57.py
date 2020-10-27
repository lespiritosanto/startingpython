# create a program that reads the gender of a person in the format [M/F].
# If its not in this format, ask again until it is right

counter = 0

gender = str(input('Are you male or female? [M/F] ')).strip().casefold()

while gender[0] not in 'mf':
    gender = str(input('Are you male or female? Please type in the format: [M/F] ')).strip().casefold()
    counter += 1

if gender[0] == 'f' or 'm':
    if gender[0] == 'f':
        print('You are female.')
    else:
        print('You are male.')

print('Number of tries: {}.'.format(counter))
