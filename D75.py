# create a program that reads 4 values and put them in a tuple
# show how many times the number 9 appears, also in which position
# the first 3 was typed and all the even numbers.

lista = (int(input('Type any integers: ')), int(input('Type any integers: ')),
         int(input('Type any integers: ')), int(input('Type any integers: ')))

counter = 0

print()

if 9 in lista:
    print('The number 9 appears {} times in the tuple.'
          .format(lista.count(9)))

print()

if 3 in lista:
    print('The number 3 appears first in the {} position.'
          .format(lista.index(3)))
else:
    print('The number 3 does not appear in the tuple.')

print()
for item in lista:
    if item % 2 == 0:
        print('Even number: {}'.format(item))
    else:
        counter += 1

    if counter == len(lista):
        print('There are no even numbers in the tuple.')
