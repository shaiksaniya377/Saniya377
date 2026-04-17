import random

a = random.randint(1, 10)
guess = 0

while guess != a:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == a:
        print("Well guessed!")
    else:
        print("Try again")

print("The number was:", a)
