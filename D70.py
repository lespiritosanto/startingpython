# create a program that reads names and prices of many products. The program must ask if
# the user wants to continue. At the end, it must show how much the added value is, how
# many products costs more than 1000 and the name of the cheapest product

counter = 0
cheapest = ' '
values = []
products = []

print('Welcome to Casas Bahia')
print('+=' * 30)

while True:
    product = str(input('Type the name of the product: ')).strip().casefold()
    value = float(input('Type the cost of the product: '))

    if value > 1000:
        counter += 1

    values.append(value)
    products.append(product)

    # test to get out of loop
    stop = str(input('Do you want to continue [y/n]? ')).strip().casefold()[0]
    print()
    if stop[0] == 'n':
        break

print('There are {} products that costs more than R$ 1000'.format(counter))
print('The cheapest product costs: R$ {:.2f}'.format(min(values)))
print("It is the {}.".format(products[values.index(min(values))]))
