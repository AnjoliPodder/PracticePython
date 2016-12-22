'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
divisor of 26 because 26 / 13 has no remainder.)
'''

def divisors(num):
    div_list = [1]
    for x in range(2,int(num/2)+1):
        if num%x == 0:
            div_list.append(x)
    div_list.append(num)
    return div_list

print(divisors(10))
print(divisors(288))
