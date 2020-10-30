# create a program that reads numbers and put them in a list.
# If the number is already there, it should not be included.
# in the end, show all numbers in a crescent order

list_num = list()
counter = 0
choice = ' '

while choice != 'n':
    list_num.append(int(input('Type an integer value: ')))
    if list_num.count(list_num[counter]) > 1:
        del list_num[counter]
        print('The number was already in the list. Cannot repeat the value.')
        print('+=' * 25)
    else:
        print('The value was added to the list.')
        print('+=' * 25)
        counter += 1

    choice = str(input('Do you want to continue? [y/n] ')).strip().casefold()[0]

print('+=' * 25)
print('The ordered numbers in the list are: '
      '{}'.format(sorted(list_num)))
print('+=' * 25)
print('You added {} numbers'.format(counter))
