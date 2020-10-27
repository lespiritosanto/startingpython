# create a program that countdown from 10 to 0 with 1 second pause between them

from time import sleep
import emoji

for num in range(10, 0, -1):
    print(num)
    sleep(1)

print(emoji.emojize(':fireworks:'))
