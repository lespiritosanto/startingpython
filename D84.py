# create a program that reads the name and age of many ppl, putting all in a list
# at the end, show how many ppl were registered; a list of the heaviest and another
# of the lightest

ppl = []
name_wei = []

while True:
    name_wei.append(str(input('Type the name: ').strip().capitalize()))
    name_wei.append(float(input('Type the weight: ')))

    ppl.append(name_wei[:])
    name_wei.clear()

    choice = input('Do you want to continue? [y/n] ').strip().casefold()
    print('=+' * 30)
    if choice == 'n':
        break

print('There were {} registered people.'.format(len(ppl)))

big = small = ppl[0][1]
for person in ppl:
    for weight in person:
        if type(weight) == float:
            if weight > big:
                big = weight
            elif weight < small:
                small = weight

print('The heaviest person is {:.2f} kg.'.format(big))
print('The lightest person is {:.2f} Kg.'.format(small))
print('=+' * 30)

print('The heaviest are: ', end='')
for person in ppl:
    if person[1] == big:
        print('{}'.format(person[0]), end=' ')

print()
print('The lightest are: ', end='')
for person in ppl:
    if person[1] == small:
        print('{}'.format(person[0]), end=' ')
