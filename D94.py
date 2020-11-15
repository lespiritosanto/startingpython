# the program must read name, sex, age of many ppl, putting each person in a dict and all dicts in
# a list. At the end show: how many ppl were registered, average age, a list of the women, a list of
# ppl higher than average age

person = dict()
ppl = []

while True:
    person['Name'] = str(input('Name: ').strip().capitalize())

    person['Sex'] = str(input('Sex [M/F]: ').strip().casefold())
    while person['Sex'] not in 'mf':
        print('ERROR! Please type only M or F. ')
        person['Sex'] = str(input('Sex [M/F]: ').strip().casefold())

    person['Age'] = int(input('Age: '))

    ppl.append(person.copy())
    person.clear()

    choice = str(input('Do you want to continue? [Y/N] ').strip().casefold()[0])
    while choice not in 'ny':
        print('ERROR! Please type only Y or N. ')
        choice = str(input('Do you want to continue? [Y/N] ').strip().casefold()[0])

    if choice == 'n':
        break

print('-=' * 35)
print(f'A) There were {len(ppl)} people registered. ')

count = 0
for i in range(0, len(ppl)):
    count += ppl[i]['Age']

average = count/len(ppl)
print(f'B) The average age is {average:.2f}. ')

women = []
for i in range(0, len(ppl)):
    if ppl[i]['Sex'] == 'f':
        women.append(ppl[i]['Name'])
print(f'C) The registered women are: {women}')

print('D) List of the people with age above average: ')
for i in range(0, len(ppl)):
    if ppl[i]['Age'] > average:
        print(f"Name: {ppl[i]['Name']}; Sex: {ppl[i]['Sex']}; Age: {ppl[i]['Age']};")

print('==' * 3, 'PROGRAM FINISHED', '==' * 3)
