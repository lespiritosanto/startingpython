# ask an integer and ask the user to choose
# binary, octal or hex to convert the number.

base_number = int(input('Give me an integer number: '))
print('+=' * 80)
print()

choice = 0
while choice not in (1, 2, 3):
    choice = int(input('''Please choose one of the number systems below:
    1. Binary
    2. Hex
    3. Octal
    '''))


binary = []
HEX = []
octal = []


# printing
# could have used bin(), oct() and hex()

if choice == 1:
    while base_number >= 2:
        binary.append(base_number % 2)
        base_number = base_number // 2

    if base_number == 1:
        binary.append(base_number)

    print(binary[::-1])
    print()

elif choice == 2:
    while base_number >= 16:
        HEX.append(base_number % 16)
        base_number = base_number // 16

    if base_number == 1:
        HEX.append(base_number)

    print(HEX[::-1])
    print()

else:
    while base_number >= 8:
        octal.append(base_number % 8)
        base_number = base_number // 8

    if base_number == 1:
        octal.append(base_number)

    print(octal[::-1])
    print()
