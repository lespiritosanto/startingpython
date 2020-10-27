# create a program that asks the date of
# birth of seven people and tell how many
# are legal adults and how many are not

from datetime import date

this_year = date.today().year

# counters
legal_adult = 0
kid = 0

for person in range(1, 8):
    year = int(input('What is the year of your birth? '))
    if (this_year - year) >= 21:
        legal_adult += 1
    else:
        kid += 1

print('There are {} legal adults and {} kids among the participants.'
      .format(legal_adult, kid))
