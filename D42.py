# ask three values for the length of lines
# and if they can form a triangle.
# if they can, classify them in equilateral,
# isosceles (two equal) or scalene (all different).

line1 = float(input('Type a value for a triangle first side: '))
line2 = float(input('Type a value for a triangle second side: '))
line3 = float(input('Type a value for a triangle third side: '))

sum1 = line1 + line2
sum2 = line1 + line3
sum3 = line2 + line3

if sum1 < line3 or sum2 < line2 or sum3 < line1:
    print('These values cant make a triangle.')
else:
    print('These values may form a triangle.')
    if line1 == line2 == line3:
        print('It forms an equilateral triangle')
    elif line1 == line2 or line1 == line3 or line2 == line3:
        print('It forms an isosceles triangle.')
    else:
        print('It forms a scalene triangle')
