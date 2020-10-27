# create a program that reads an integer n and shows the first n
# elements of the fibonacci sequence

n = int(input('Please type an integer number '))

first = 0
second = 1
iteraction = 3

print('{}'.format(first), end=' -> ')
print('{}'.format(second), end=' -> ')

while iteraction <= n:
    third = first + second
    print('{}'.format(third), end=' -> ')
    first = second
    second = third
    iteraction += 1

print('End')
