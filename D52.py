# create a program to read an integer and tell if he is prime

num = int(input('Type an integer number: '))
divi = []

for i in range(1, num + 1):
    if num % i == 0:
        divi.append(i)

if len(divi) > 2:
    print('The number {} is not prime.'.format(num))
elif len(divi) == 1:
    print('The number {} is not a prime.'.format(num))
else:
    print('The number {} is prime.'.format(num))
