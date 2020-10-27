# create a program to read six integers and
# show the even ones and their sum

even = []
num_sum = 0

for i in range(0, 6):
    num = int(input('Type an integer number: '))
    if num % 2 == 0:
        even.append(num)
        num_sum += num

print()
print('The numbers that are even are: {} and their sum is {}.'
      .format(even, num_sum))
