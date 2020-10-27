# create a program that the computer thinks of a number in the range(0,11)
# and the player can keep guessing until he gets it right, and the program
# should also count and report the tries

from random import randint

guess_counter = 0
computer_guess = randint(0, 10)

print('I am going to think of a number from 0 to 10 and you should guess it!')
player_guess = int(input('Please think of a number between 0 and 10: '))

while player_guess != computer_guess:
    guess_counter += 1
    if player_guess < computer_guess:
        print('A little more...')
        player_guess = int(input('Please think of a number between {} and 10: '
                                 .format(player_guess)))
    if player_guess > computer_guess:
        print('A little less...')
        player_guess = int(input('Please think of a number between {} and 0:'
                                 .format(player_guess)))

if guess_counter == 0:
    print('You guessed it first time!')
else:
    print('You guessed it right in {} times'.format(guess_counter))
