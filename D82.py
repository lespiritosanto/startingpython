# create a program that reads many numbers, put them in a list.
# after that, create 2 additional lists. One must have odd values and
# the other even values. At the end, print the 3 lists

numbers = list()
numbers_even = list()
numbers_odd = list()

while True:
    numbers.append(int(input('Type a number to add the list: ')))
    print('+=' * 30)

    choice = str(input('Do you want to continue? [y/n] ')).strip().casefold()[0]
    print('+=' * 30)
    if choice[0] == 'n':
        break

for item in numbers:
    if item % 2 == 0:
        numbers_even.append(item)
    else:
        numbers_odd.append(item)

print('The original list is {}'.format(numbers.sort()))
print('+=' * 30)
print('The list with even numbers is {}'.format(numbers_even.sort()))
print('+=' * 30)
print('The list with odd numbers is {}'.format(numbers_odd.sort()))
