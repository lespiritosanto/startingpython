# program must read name, age, and
# gender (masc or fem) of 4 people
# should also show the average age,
# the name of the oldest and how many
# women are less then 20 years

average = 0
oldest = 0
woman_count = 0
oldest_name = ''

for i in range(1, 5):
    name = str(input('What is your name? '))
    age = int(input('Please type your age: '))
    sex = str(input('Please type your gender (M or F): ')).strip().upper()
    average += age
    if i == 1 and sex in 'Mm':
        oldest += age
        oldest_name += name
    if sex in 'Mn' and age > oldest:
        oldest_name = name
        oldest = age
    if sex in 'Ff' and age < 20:
        woman_count += 1

print()
print('The average age is {}'.format(average/4))
print('The oldest is {} years old and his name is {}'.format(oldest, oldest_name))
print('The amount of women that are 20 or less is {}'.format(woman_count))
