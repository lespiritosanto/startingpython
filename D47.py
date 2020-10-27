# create a program that shows all even numbers in the range from 1 to 50

print('+=' * 10)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

print('+=' * 10)

# or i could have used, it would save some memory

# for i in range(2, 51, 2):
#     print(i)
