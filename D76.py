# create a program that has only one tuple with the names and prices of products, in sequence
# at the end, show the data organized in a list of products and prices


lista = (('Monitor', 2000), ('Mouse', 250), ('Keyboard', 450), ('DVD Player', 50),
         ('Graphic Card', 2500), ('RAM', 1200), ('Motherboard', 1300))

print('\033[30;41m+=\033[m' * 20)
print('{:^40}'.format('Computer Parts List'))
print('\033[30;41m+=\033[m' * 20)

for item in lista:
    print('{:.<28} R$ {:>7.2f}'
          .format(item[0], item[1]))

print('\033[30;41m+=\033[m' * 20)
