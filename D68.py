# create a program that plays even or odds with the user
# the game stops when the player loses, and shows the number of wins

from random import randint

counter = 0

while True:
    cp_num = randint(1, 1000)
    num = int(input('Lets play even or odds! Type a number: '))
    added = cp_num + num

    while True:
        choice = str(input('Do you want even or odd? [e/o] ')).strip().casefold()[0]
        if choice[0] in 'eo':
            break

    # check if the sum of the numbers are even or odd
    if added % 2 == 0:
        print('You chose {} and I chose {}. Together they result in an even number'
              .format(num, cp_num))
        if choice == 'e':
            print('You win!')
            counter += 1
        elif choice == 'o':
            counter += 1
            print('You lose! You lost in {} tries.'.format(counter))
    else:
        print('You chose {} and I chose {}. Together they result in an odd number'
              .format(num, cp_num))
        if choice == 'e':
            print('You win!')
            counter += 1
        elif choice == 'o':
            counter += 1
            print('You lose! You won {} games straight.'.format(counter))
            break

