# create a program that reads 5 values and put them in a list.
# show the biggest and lowest value typed and their respective position

lista = []

for item in range(0, 5):
    lista.append(float(input('Please type a number: ')))

print('+=' * 25)
print('The biggest value is {}. Position...'.format(max(lista)), end='')
for i, value in enumerate(lista):
    if value == max(lista):
        print('{}...'.format(i), end='')

print('\n', '+=' * 25)
print('The lowest value is {}. Position...'.format(min(lista)), end='')
for i, value in enumerate(lista):
    if value == min(lista):
        print('{}...'.format(i), end='')

print('\n', '+=' * 25)
