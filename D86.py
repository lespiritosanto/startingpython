# create a program that declares a matrix 3x3 and fills it with values
# typed by the user. At the end, show the matrix in the screen

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for g in range(0, 3):
        matrix[l][g] = int(input('Type a number to add to the position ({},{}) of the matrix: '
                                 .format(l, g)))

print('+=' * 20)
for item in range(0, 3):
    print(matrix[item])
