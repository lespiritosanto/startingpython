# create a program that receives numbers and put them in a list.
# It should show how many numbers were put in the list, print the list
# in decreasing order, and if the value 5 was typed or if it is or not in the list

numbers = []
choice = ' '
counter = 0

while choice[0] != 'n':
    numbers.append(int(input('Type a number to add to the list: ')))

    print('+=' * 30)
    counter += 1
    choice = str(input('Do you want to continue adding numbers? [y/n] ')).strip().casefold()[0]

print('+=' * 30)
print('There were {} numbers put in the list.'.format(counter))

print('+=' * 30)
print(sorted(numbers, reverse=True))

print('+=' * 30)
if 5 in numbers:
    print('The number {} was typed and added to the list.'.format(5))
else:
    print('The number 5 is not in the list.')
