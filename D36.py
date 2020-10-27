# write a program to give a loan to buy a house.
# Ask house value, worker wage and installments.
# If the installment exceeds 30% of the worker salary,
# the loan should no be accepted.

print('=+' * 10, '\033[7;30;41mLoan Interface\033[m', '=+' * 10)
print()

# variables
house_value = float(input('What is the property value, in dollars? '))
salary = float(input('What is your wage? U$ '))
installments = int(input('How many monthly installments do you require? '))
monthly_debit = house_value / installments
print()

if monthly_debit > (salary * 0.3):
    print('''Unfortunately your loan is not approved. 
    The asked conditions exceed 30% of your monthly wage''')
    print('Installment value is: {}'.format(monthly_debit))
else:
    print('Your loan is approved. The monthly installment amounts: {:.2f} dollars'
          .format(monthly_debit))
