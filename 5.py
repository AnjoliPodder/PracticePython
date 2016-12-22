'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

def common(list1, list2):
    com = []
    if len(list2) < len(list1):
        list2, list1 = list1, list2
    for el in list1:
        if el in list2 and not(el in com):
            com.append(el)
    return com


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common(a, b))
