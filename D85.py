# create a program that the user types 7 numeric values and put them in a list.
# even and odds values must be separated. At the end, print them in crescent order

even = []
odds = []
values = [even, odds]

for val in range(0, 7):
    num = int(input('Type the {}° numeric value: '.format(val + 1)))
    if num % 2 == 0:
        values[0].append(num)
    else:
        values[1].append(num)

even.sort()
odds.sort()
print('+=' * 25)
print('The even numbers are: {}.'.format(values[0]))
print('The odd numbers are: {}.'.format(values[1]))
print('+=' * 25)
