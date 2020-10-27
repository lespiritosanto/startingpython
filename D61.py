# recreate exercise 51, making the program show the first 10
# terms of the arithmetic progression using while

ratio = float(input('Please type the ratio of the AP: '))
term = float(input('Please type the first term of the AP: '))
count = 1

while True:
    if count == 11:
        break
    print('the {}° term of the AP is: {}'.format(count, term + ratio * (count - 1)))
    count += 1


