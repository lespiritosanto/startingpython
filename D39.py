# ask for a birth date.
# Show if the person has to enroll for the military
# 17 should enlist, 18 years old should be present themselves,
# more than that already enrolled. The program should also show
# the time in years that are needed to present or that passed

from datetime import date

year = int(input('What year were you born? '))
current_year = date.today().year
age = current_year - year

sex = input('Are you male or female? ').strip().lower()

if sex == 'male':
    if age == 18:
        print('You should present yourself to the military this year')
    elif age == 17:
        print('You should enlist to the military to serve next year')
    elif age < 17:
        print('Too soon for you. You still need to wait {} years to serve.'
              .format(18 - age))
    else:
        print('You already served the country {} years ago.'
              .format(age - 18))
elif sex == 'female':
    print("In Brazil you don't need to serve the military")
else:
    print('You should type "male" or "female".')
