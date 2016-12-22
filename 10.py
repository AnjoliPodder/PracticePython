'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python
or using at least one list comprehension
'''

def common(list1, list2):
    return [x for x in set(list1 + list2) if x in list1 and x in list2]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common(a, b))