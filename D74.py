# create a program that generates 5 random numbers and put them inside a tuple
# after that, show the list of generated numbers and show the biggest and lowest value
# of the numbers in the tuple

from random import randint

tup = (randint(0, 100), randint(0, 100), randint(0, 100),
       randint(0, 100), randint(0, 100))

for i in tup:
    print(i, end=' ')


print('\nThe biggest number is {}'.format(max(tup)))
print('+=' * 20)
print('The lowest number is {}'.format(min(tup)))
