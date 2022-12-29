import random
colors = ["red", "white", "black", "yellow", "pink"]

randomColorIndex =  random.randint(0, len(colors)-1)
randomColor = colors[randomColorIndex]

userColor = input("Enter a color to guess: ")

while True:
    if (userColor == randomColor):
        print("You got it!")
        break
    else:
        userColor = input("Try again: ")
    
