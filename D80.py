# create a program that reads 5 values and put them already sorted in a list and print them
# cannot use the sort() function

numbers = []


for i in range(0, 5):
    a = int(input('Type the {}° number to add to the list: '.format(i + 1)))
    if i == 0 or a > numbers[-1]:
        numbers.append(a)
    else:
        position = 0
        while position < len(numbers):
            if a <= numbers[position]:
                numbers.insert(position, a)
                break
            position += 1


print('+=' * 30)
print(numbers)
