# create a program that reads two grades from students and put them in a compost list
# at the end, show the bulletin with the average grade of each and also permits the user
# to check each student's grade individually

classroom = []
student = []

while True:
    student.append(str(input('Name of the student: ').strip().capitalize()))
    student.append(float(input('Grade 1: ')))
    student.append(float(input('Grade 2: ')))

    classroom.append(student[:])
    student.clear()
    print('-=' * 20)
    choice = str(input('Do you want to add another student? [y/n] ').strip().casefold())
    print('-=' * 20)
    if choice == 'n':
        break

print('N°: Student = Average Grade ')
print('-' * 25)
for index, person in enumerate(classroom):
    print(f'{index + 1}°: {person[0]} = {(classroom[index][1] + classroom[index][2])/2} ')

while True:
    print('+-' * 25)
    n = int(input("Do you want to see which student's grade? [0 to quit] "))
    if n == 0:
        break
    if n not in range(len(classroom) + 1):
        print("Please choose the number of the student as indicated in the table above. ")
        continue

    print(f'The grades of {classroom[n - 1][0]} are {classroom[n - 1][1]} and {classroom[n - 1][2]}. ')
