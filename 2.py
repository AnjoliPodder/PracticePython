'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def odd_or_even():
    num = int(input("Please enter a number:"))
    if num % 2 != 0:
        print("%i is odd" % num)
    elif num % 4 == 0:
        print("%i is even and divisble by 4" % num)
    else:
        print("%i is even" % num)

def check_divisible():
    num = int(input("Please enter a number:"))
    check = int(input("Please enter another number:"))
    if num % check == 0:
        print("%i divides evenly by %i" % (num, check))
    else:
        print("%i does not divide evenly by %i" % (num, check))