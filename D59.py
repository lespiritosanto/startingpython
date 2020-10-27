# create a program that reads two values and shows a menu
# with options: sum, multiply, bigger than, new numbers or exit
# obviously it should also run the functionalities

from time import sleep

first = float(input('Please type the first number: '))
second = float(input('Please type your second number: '))
choice = 0


while True:
    choice = int(input('''Please choose one of the options below:
1. Sum
2. Multiply
3. Bigger than
4. New numbers
5. Exit program
'''))
    if choice == 1:
        print('The sum of {:.2f} and {:.2f} is: {:.2f}'
              .format(first, second, first + second))
        print('+=' * 20)
    elif choice == 2:
        print('{:.2f} multiplied by {:.2f} is: {:.2f}'
              .format(first, second, first * second))
        print('+=' * 20)
    elif choice == 3:
        if first > second:
            print('{} is bigger than {}'.format(first, second))
            print('+=' * 20)
        elif first == second:
            print('{} is equal to {}'.format(first, second))
            print('+=' * 20)
        else:
            print('{} is bigger than {}.'.format(second, first))
            print('+=' * 20)
    elif choice == 4:
        first = float(input('Please type the first number: '))
        second = float(input('Please type your second number: '))
        print('+=' * 20)
    else:
        print('Exiting program...')
        print('+=' * 20)
        sleep(2)
        exit()
