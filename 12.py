'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.
'''

def firstlast(list):
    if len(list) < 2:
        return list
    else:
        return [list[0], list[-1]]

a = [5, 10, 15, 20, 25]

print(firstlast(a))
