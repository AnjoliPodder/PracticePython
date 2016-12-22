'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
that takes this list a and makes a new list that has only the even elements of this list in it.
'''


def evens(nums):
    return [x for x in nums if x % 2 == 0]

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens(a))