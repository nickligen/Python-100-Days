import random

answer = random.randint(1,100)
count = 0

while True:
    count=count+1
    number=int(input('Guess a number:'))
    if number>answer:
        print('Bigger than answer')
    elif number<answer:
        print('Smaller than answer')
    else:
        print('You are correct!')
        break

print('The answer is ' +str(number))
print('You tried ' + str(count) + ' times')
