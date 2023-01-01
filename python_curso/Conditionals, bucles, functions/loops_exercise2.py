import random
colors = ["red", "white", "black", "yellow", "pink"]

randomColorIndex =  random.randint(0, len(colors)-1)
randomColor = colors[randomColorIndex]

userColor = input("Enter a color to guess: ")
tries = 1

while True:
    if (userColor == randomColor):
        print("You got it! in ", tries, " tries")
        break
    else:
        userColor = input("Try again: ")
        tries = tries + 1
    
