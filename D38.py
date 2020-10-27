# read two integers and compare them.
# Print which value is higher than the
# other, or show that they are equal

first_value = int(input('Please give me an integer number: '))
second_value = int(input('Please give me a second integer number: '))

if first_value > second_value:
    print('{} is the largest number.'.format(first_value))
elif second_value > first_value:
    print('{} is the largest number.'.format(second_value))
else:
    print('Both numbers are equal')
