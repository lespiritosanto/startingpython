# receive birth date or age and classify the person in the categories below:
# < 9: infant
# > 9 < 14: baby
# > 14 < 19: junior
# > 19 < 25: senior
# 25 > master

from datetime import date

year = int(input('What year were you born? '))
age = date.today().year - year

if age < 9:
    print('You are at the infant category.')
elif age < 14:
    print('You are at the baby category.')
elif age < 19:
    print('You are at the junior category')
elif age < 25:
    print('You are at the senior category')
else:
    print('You are at the master category')
