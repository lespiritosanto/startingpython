# program that reads the first term and the
# ratio of an arithmetic progression.
# Show the 10 first terms

first_term = float(input('Type the first term of the arithmetic progression: '))
ratio = float(input('What is the ratio of the AP? '))

for i in range(1, 11):
    print('The {}° term of the AP is: {:.2f}.'.format(i, first_term + ratio * (i - 1)))
