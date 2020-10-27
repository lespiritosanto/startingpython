# create a program to read any sentence
# and tell if it is a palindrome

sentence = str(input('Type anything: ')).strip().casefold()

sentence.split()

sentence_no_space = ''.join(sentence)

# sentence_no_space = sentence.split()
#
# for char in sentence:
#     if char in 'abcdefghijklmnopqrstuvwxyz':
#         sentence_no_space += char

if sentence_no_space == sentence_no_space[::-1]:
    print('The sentence is a palindrome.')
else:
    print('The inverted sentence is: {}'
          .format(sentence_no_space[::-1]))
    print('The sentence is not a palindrome.')
