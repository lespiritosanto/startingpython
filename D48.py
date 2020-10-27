# create a program that calculates the sum of all
# odd numbers that are multipliable by 3 in the range
# from 1 to 500

total = 0

print('+=' * 10)
for i in range(3, 501, 2):  # Step to get odd numbers only
    if i % 3 == 0:
        total += i

print(total)
