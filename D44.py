# ask for price and payment options
# money or check - 10% discount
# 1x in credit card - 5% discount
# 2x credit card - normal price
# 3x credit card - 20% total interest

price = float(input('Type the price of the product: '))

options = 0

while options not in range(1, 5):
    options = int(input('''Choose of option from below:
    1. money or check = 10% discount
    2. one time in credit card = 5% discount
    3. two times in credit card = normal price
    4. three times in credit card = 20% total interest
    '''))

print()

if options == 1:
    print('The final price is: U${:.2f}'.format(price * 0.9))
elif options == 2:
    print('The final price is: U${:.2f}'.format(price * 0.95))
elif options == 3:
    print('The final price is: U${:.2f} and the monthly installment is U${:.2f}'
          .format(price, price / 2))
else:
    print('The final price is: U${:.2f} and the monthly installment is U${:.2f}'
          .format(price * 1.2, (price * 1.2) / 3))
