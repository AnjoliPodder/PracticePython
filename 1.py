'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous
message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime

def year_100():
    name = input("Please enter your name:")
    age = input("Please enter your age:")
    year_at_100 = 100 - int(age) + datetime.datetime.now().year
    print("Hi %s, The year when you are 100 will be %i" %(name, year_at_100))
    num = input("Now, enter a number:")
    print(("Hi %s, The year when you are 100 will be %i \n" %(name, year_at_100))*int(num))