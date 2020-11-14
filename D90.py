# create a program that reads the name and average grade of a student. Put all in a dict
# and show at the end also if he is approved or not

student = dict()

student['Name'] = str(input('Name of the student: ').strip().capitalize())
student['Average'] = float(input('Average grade of the student: '))

if student['Average'] > 5:
    student['Situation'] = 'Approved'
else:
    student['Situation'] = 'Reproved'

print('-=' * 25)
for k, val in student.items():
    print(f'{k} is {val}.')
