# create a program that read age and sex of many people. At each person registered
# the program must ask if they want to continue with the register
# at the end it should show how many people have more than 18, how many men
# and how many women have less than 20

sex_count = man_age_count = women_age_count = age_count = 0
choice = ''

while True:
    print('+=' * 25)
    age = int(input('Type your age: '))
    if age > 18:
        age_count += 1

    sex = str(input('Type your gender [m/f]: ')).strip().casefold()[0]
    while sex[0] not in "mf":
        sex = str(input('Type your gender [m/f]: ')).strip().casefold()[0]

    if sex == 'm' and age < 18:
        man_age_count += 1

    if sex == 'f' and age < 18:
        women_age_count += 1

    choice = input('Do you want to continue with the register [y/n]? ').strip().casefold()[0]
    if choice[0] == 'n':
        break
print('There are {} adults, {} men and {} women have less than 18.'
      .format(age_count, man_age_count, women_age_count))
