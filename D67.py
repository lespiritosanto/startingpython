# create a program that shows a taboada of many numbers, one at a time
# if the input is negative, stops the program

num = counter = 0

while True:
    num = int(input('Please type a number (negative numbers end the program): '))

    # condition to go out of the loop
    if num < 0:
        break

    print('+=' * 20)
    for item in range(1, 10):
        print('{} x {} = {}'.format(num, item, num * item))
    print('+=' * 20)
