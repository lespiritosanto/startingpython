# the program must read name, date of birth and worker permit number and put them in a dict
# with age as one of the parameters. If the wpn is != than 0, the dict should also receive
# year of contract and monthly wage. At the end, also show when the person will retire, considering
# 35 years of contribution

from datetime import datetime

person = {'Name': str(input('Name: ').strip().capitalize()),
          'Date': int(input('Date of Birth: ')),
          'Work Permit': int(input('Work Permit Number [0 to finish]: '))
          }

person['Age'] = datetime.now().year - person['Date']

if person['Work Permit'] == 0:
    print('+=' * 30)
    for key, value in person.items():
        print(f'{key} is {value}.')
    exit()
else:
    person['Year of the contract'] = int(input('Year of the contract: '))
    person['Salary'] = float(input('Salary: R$ '))
    person['Retirement'] = (person['Year of the contract'] - person['Date']) + 35
    del person['Date']
    print('-=' * 30)
    for key, value in person.items():
        print(f'  == {key} is {value}.')
