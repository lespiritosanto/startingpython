# create a program that read integers and stops if 999 is typed
# count and sum the tries

addition = count = value = 0

while True:
    value = int(input('Please type a number (999 to stop): '))

    if value == 999:
        break

    count += 1
    addition += value

print('The number of tries were {:.2f} and the sum of the number is {:.2f}.'
      .format(count, addition))
