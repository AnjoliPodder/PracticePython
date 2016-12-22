'''
Solution by: Anjoli Podder
December 2016

http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity
to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to
generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the
previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fib(num):
    fib_list = [1,1]
    if num == 1:
        return [1]
    elif num == 2:
        return fib_list
    else:
        for i in range(3,num+1):
            fib_list.append(fib_list[-1]+fib_list[-2])
        return fib_list


print(fib(5))
print(fib(10))
print(fib(100))
