# ask for height and weight of a person and calculate BMI
# < 18.5 = low weight
# > 18.5 but < 25 = ideal weight
# > 25 but < 30 = overweight
# > 30 but < 40 = obesity
# > 40 = morbid obesity

hei = float(input('Type your height in meters: '))
wei = float(input('Type your weight in kilograms: '))
print()

BMI = wei / hei ** 2  # formula

if BMI < 18.5:
    print('Your weight is too low')
elif 18.5 <= BMI < 25:
    print('Your weight is ideal')
elif 25 <= BMI < 30:
    print('You are \033[4moverweight\033[m.')
elif 30 <= BMI < 40:
    print('You have \033[4mobesity\033[m')
else:
    print('You have \033[4mmorbid obesity\033[m!')

print('\033[7;30;41mYour BMI is {:.2f}\033[m'.format(BMI))
