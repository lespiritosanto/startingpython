# create a program that reads an integer and makes its factorial
# try to use for and while

num = int(input('Please type an integer number: '))
result = 1

while num > 1:
    result *= num
    num -= 1

print(result)

# using for loop

# f = 1
# for i in range(1, num + 1):
#     f *= num
#     num -= 1
#
# print(f)
