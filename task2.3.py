from random import randint

rand = randint(1, 10)
numb = input('Guess the number from 1 to 10: ')

if numb != rand:
    while numb != rand:
        numb2 = int(input('Try another one: '))
        if numb2 == rand:
            print('Good boy. You guessed right!')
            break
else:
    print('On the first try. Well done!')
