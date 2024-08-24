import random

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll: "))
if guess == roll:
    print("Right guess!")
else:
    print("Wrong guess!")
print("The dice roll was", roll)
