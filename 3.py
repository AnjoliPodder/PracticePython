'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than
that number given by the user.
'''

def less_than_5(input_list):
    num = int(input("Please enter a number: "))
    return [x for x in input_list if x < num]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(less_than_5(a))
print(less_than_5(a))
