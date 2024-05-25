#Exercise: Loops Second One - Color Guesser

import random
print("Color Guesser 3000")

colors = ["red", "magenta", "black", "yellow", "blue", "white", "grey", "pink"]

ToBeContinued = "yes";
guess = "y";

while ToBeContinued == "yes":
    color = random.choice(colors)
    guess = input("Now, Guess The Right Color: ").lower()
    if guess != color:
        guess == input("Nope. Try Again Now: ").lower()
    else:
        print("You Have Guessed Right! It was", color)
        ToBeContinued = input("Do You Want To Continue Playing? Yes/No\n").lower()
print("Game Over.")    
    
'''
#Video Code:
import random
colors = ["white", "black", "red", "green", "blue", "yellow", "purple", "grey"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if(color == guess.lower()):
            break
        else:
            guess = input("Nope. Try again: ")
    print("You guessed it! I was thinking about", color)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == 'no':
        break
print("It was fun, thanks for playing!")
'''
