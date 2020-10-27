# create a number taboo with the new techniques

num = int(input('Please type an integer number: '))

for i in range(1, 10):
    print('{} times {} is {}.'.format(num, i, num * i))
