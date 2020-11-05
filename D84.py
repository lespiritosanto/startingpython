# create a program that reads the name and age of many ppl, putting all in a list
# at the end, show how many ppl were registered; a list of the heaviest and another
# of the lightest

people = []
choice = ' '

while choice != 'n':
    people.append(str(input('Type your name: ').strip().capitalize()))
    people.append(int(input('Type your weight: ')))
    print('+=' * 25)

    choice = str(input('Do you want to continue? [y/n] ')).strip().casefold()

print('The number of people registered were: {}.'.format(len(people) // 2))

maximum = 0
for char in people:
    if type(char) == int:
        if people[1] == char:
            lightest = char
        if char > maximum:
            maximum = char
        if char < lightest:
            lightest = char

print('The heaviest person is: {}'.format(people[people.index(maximum) - 1]))

print('The lightest person is: {}'.format(people[people.index(lightest) - 1]))
