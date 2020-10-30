# create a program where the user will add numbers and put them in a list
# already sorted, without using the function sort(). Show the result at the end

numbers = list()
sorted_list = list()
choice = ' '

while choice[0] != "n":
    numbers.append(int(input('Type a number to add to the list: ')))

    choice = str(input('Do you want to continue adding numbers? [y/n] ')).strip().casefold()[0]

while len(numbers) != 0:
    sorted_list.append(min(numbers))
    numbers.remove(min(numbers))

print('+=' * 30)
print(sorted_list)
