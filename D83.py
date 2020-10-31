# create a program where the user will type any mathematical expression
# and the result must be if it is written right or wrong

expression = [input('Type a mathematical expression: ').casefold()]
counter_left = 0
counter_right = 0

for item in expression:
    for c in item:
        if '(' in c:
            counter_left += 1
        if ")" in c:
            counter_right += 1

if counter_left != counter_right:
    print('+=' * 25)
    print('The expression is wrong.')
else:
    print('+=' * 25)
    print('The expression is right.')
