# create a program that has a tuple with written numbers from 0 to 20
# The user will type a value and it should return it written

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven'
           , 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
           'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
           'nineteen', 'twenty')

while True:
    # choosing a number in the range we want
    val = int(input('Please choose a number from 0 to 20: '))
    while val not in range(0, 21):
        val = int(input('Please choose a number from 0 to 20: '))

    print('The number you chose was: {}.'.format(numbers[val]))

    # exiting the loop
    choice = str(input('Do you want to continue? [y/n] ')).strip().casefold()[0]
    if choice[0] == 'n':
        break

