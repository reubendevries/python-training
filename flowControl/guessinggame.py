import random

lowest = 1
highest = 1000
answer = random.randint(lowest,highest)
guess = 0

print("Please guess a number between {} and {}: ".format(lowest,highest))
while guess != answer:
        guess = int(input())
        if guess == answer:
            print("Well done you got it!")
            break
        elif guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")