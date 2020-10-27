# create a program that reads the weight of
# 5 people and tell which is the heaviest and
# who is lightest

base = []

for people in range(1, 6):
    wei = float(input('Type your weight (kg): '))
    base.append(wei)

print('The heaviest is {}kg and the lightest is {}kg'
      .format(max(base), min(base)))
