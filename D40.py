# create a program that calculates students grades and
# also returns if they passed (7 or higher), are in
# probation (5 to 6.99) or failed.

name = str(input('Type the name of the student: '))
first_grade = float(input('Type the first grade: '))
second_grade = float(input('Type the second grade: '))
score = (first_grade + second_grade) / 2

if score < 5:
    print('The student {} failed the class. He scored {:.2f}.'.format(name, score))
elif score < 7:
    print('The student {} is on probation. He scored {:.2f}.'.format(name, score))
else:
    print('The student {} passed. He scored {:.2f}.'.format(name, score))
