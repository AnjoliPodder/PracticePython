'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome("tacocat"))