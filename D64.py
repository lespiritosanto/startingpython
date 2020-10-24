# recreate exercise 61, asking the user if he wants
# the program to calculate more terms. The program should
# end if the user writes 0

ratio = float(input('Type the ratio of the AP: '))
term = float(input('Type the first term of the AP: '))
counter = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while counter <= total:
        print('The {}° term of the AP is: {}'.format(counter, term + ratio * (counter - 1)))
        counter += 1

    more = int(input('How many terms you want more? '))




