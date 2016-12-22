'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
that takes this list a and makes a new list that has only the even elements of this list in it.
'''

def rps():
    print("Welcome to the game! Your move must be rock, paper or scissors.")
    valid_moves = ["rock", "paper", "scissors"]
    valid1 = False
    valid2 = False
    pl1 = ""
    pl2 = ""
    while not(valid1):
        pl1 = input("Please enter your move, Player 1: ").lower()
        if not(pl1 in valid_moves):
            print("That was not a valid move. Try again.")
        else:
            valid1 = True
    while not(valid2):
        pl2 = input("Please enter your move, Player 2: ").lower()
        if not(pl2 in valid_moves):
            print("That was not a valid move. Try again.")
        else:
            valid2 = True
    if pl1 == pl2:
        print("You both chose", pl1,". It's a tie!")
    elif (pl1, pl2) == ("rock", "paper"):
        print("Player 2 Wins! Rock is wrapped by Paper")
    elif (pl1, pl2) == ("rock", "scissors"):
        print("Player 1 Wins! Rock breaks Scissors")
    elif (pl1, pl2) == ("paper", "scissors"):
        print("Player 2 Wins! Paper is cut by Scissors")
    elif (pl1, pl2) == ("paper", "rock"):
        print("Player 1 Wins! Paper wraps Rock")
    elif (pl1, pl2) == ("scissors", "paper"):
        print("Player 1 Wins! Scissors cuts Paper")
    elif (pl1, pl2) == ("scissors", "rock"):
        print("Player 2 Wins! Scissors is broken by Rock")
    again = input("Do you want to play again? (Y/N): ").lower()
    if again == "y":
        rps()
    else:
        print("Thanks for playing!")
        pass

rps()