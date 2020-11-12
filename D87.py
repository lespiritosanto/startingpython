# create a program that upgrades D86.py and show the sum of all digited values
# also show the sum of the values of the third column
# also show the biggest value of the second line

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for g in range(0, 3):
        matrix[l][g] = int(input('Type a number to add to the position ({},{}) of the matrix: '
                                 .format(l, g)))

print('+=' * 20)

added = 0

for l in range(0, 3):
    for g in range(0, 3):
        print(f'[{matrix[l][g]}]', end=' ')
        added += matrix[l][g]
    print()

print('+=' * 20)

third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]

print(f'The sum of the values is: {added:.2f}. ')
print(f'The biggest value in the second line of the matrix is {max(matrix[1])}. ')
print(f'The sum of values in the third column is {third_column}. ')
