# create a program that reads multiple integer numbers. Calculate the average of them
# and also tell which number is the biggest and also the lowest. The program should also
# ask the user if he wants it to continue

first = second = average = counter = soma = 0
answer = 'yes'


while answer[0] != 'n':
    first = int(input('Please type a first integer number: '))
    second = int(input('Please type a second integer number: '))
    average = (first + second) / 2

    if first > second:
        print('{} is the biggest number and {} the lowest'.format(first, second))
    elif first == second:
        print('{} and {} are equal'.format(first, second))
    else:
        print('{} is the biggest number and {} the lowest'.format(second, first))

    print('The average between {} and {} is {}.'.format(first, second, average))
    print('+=' * 25)
    answer = str(input('Do you want to continue [y/n] ')).strip().casefold()
