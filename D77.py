# create a program that has a tuple with many words and show, for each word, their
# vowels

words = ('house', 'car', 'computer', 'room', 'keyboard',
         'beaches', 'pharmacy', 'university', 'notebook')

print('+=' * 25)
for item in words:
    print('The word {} has this vowels:'.format(item), end=' ')
    for char in item:
        if char in 'aeiou':
            print('{}'
                  .format(char), end=' ')
    print()
print('+=' * 25)

