'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
number is a number that has no divisors.). You can (and should!) use your answer to [Exercise 4] to help you.
Take this opportunity to practice using functions, described below.
'''

def divisors(num):
    div_list = [1]
    for x in range(2,int(num/2)+1):
        if num%x == 0:
            div_list.append(x)
    div_list.append(num)
    return div_list

def is_prime(num):
    return len(divisors(num)) == 2

print(is_prime(7))
print(is_prime(100))
print(is_prime(1000))
print(is_prime(107234))