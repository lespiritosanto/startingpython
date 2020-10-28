# create a program that simulates the working of a cash machine. If must ask for the value of
# withdraw (integer) and return the number of banknotes. Consider notes of 50, 20, 10 and 1

print('+=' * 30)
print('Welcome the the BANK')
print('+=' * 30)

while True:
    while True:
        value = int(input('Type the value to be withdrawn: R$ '))
        if value == 0:
            print('You cannot withdraw this amount. Try again. ')
        if value < 0:
            print('The value should be positive. Try again. ')
        else:
            break

    notes_50 = value // 50
    notes_20 = (value % 50) // 20
    notes_10 = ((value % 50) % 20) // 10
    notes_1 = (((value % 50) % 20) % 10) // 1

    print('Returning {:.0f} notes of R$ 50.'.format(notes_50))
    print('Returning {:.0f} notes of R$ 20.'.format(notes_20))
    print('Returning {:.0f} notes of R$ 10.'.format(notes_10))
    print('Returning {:.0f} notes of R$ 1.'.format(notes_1))
    print('=+' * 30)

    choice = str(input('Are you finished? [y/n] ')).strip().casefold()[0]

    if choice[0] == 'y':
        break
