#NumberGuesser
#number = 5
import random

number =  random.randint(0,10)

guess = int(input("I'm thinking about a number between zero and ten. Can you guess it? "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope. Try Again Now: "))
print("You guessed it. I was thinking about", number)
