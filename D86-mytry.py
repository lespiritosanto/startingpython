# create a program that declares a matrix 3x3 and fills it with values
# typed by the user. At the end, show the matrix in the screen

matrix = [[], [], [],
          [], [], [],
          [], [], []]

for i in range(0, 9):
    matrix[i].append(int(input('Type the {}° number of the matrix: '.format(i + 1))))

print('+=' * 20)

counter = 0

for i in range(0, 9):
    if counter == 3 or counter == 6:
        print()
    print(matrix[i], end=' ')
    counter += 1
