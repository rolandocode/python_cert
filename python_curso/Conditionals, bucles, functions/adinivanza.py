import random
number = random.randint(0,10)

guess = int (input("Im thinking in a number, can you guess? "))

while True:
    if (guess == number):
        print("Yes, you got it!")
        break
    else:
        guess = int (input("guess again "))