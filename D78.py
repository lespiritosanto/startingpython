# create a program that reads 5 values and put them in a list.
# show the biggest and lowest value typed and their respective position

lista = []

for item in range(0, 5):
    lista.append(float(input('Please type a number: ')))

print('+=' * 25)
print('The biggest value is {} and it is {}° in the list.'
      .format(max(lista), lista.index(max(lista)) + 1))
print('+=' * 25)
print('The lowest value is {} and it is {}° in the list.'
      .format(min(lista), lista.index(min(lista)) + 1))
print('+=' * 25)
