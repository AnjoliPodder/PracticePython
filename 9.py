'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

def guess_number():
    num = random.randint(1,9)
    guesses = 0
    right = False
    while not(right):
        guess_str = input("Guess the secret number between 1 and 9 or type exit to end:")
        if guess_str.lower() == "exit":
            print("Game ended. Bye for now.")
            break
        else:
            try:
                guess = int(guess_str)
                if guess > 9 or guess < 1:
                    print("Invalid input - please try again")
                elif guess > num:
                    print("Too high!")
                    guesses += 1
                elif guess < num:
                    print("Too Low!")
                    guesses += 1
                else:
                    guesses += 1
                    if guesses > 1:
                        print("You guessed right! The secret number was %i. It took you %i guesses." % (guess,guesses))
                    else:
                        print("You guessed right! The secret number was %i. It took you %i guess." % (guess, guesses))
                    right = True
            except:
                print("Invalid input - please try again")


guess_number()