# Name: Jamar Hill
# Date: 10/21/2020
# Description: Project 4.b

def fib(n): #Describe "n" as a variable in fib sequence
    """This Fuction returns the value to a position of a number in a Fibonacci sequence"""
    while n == 0:
       return 0 #establish that 0 position is equal to 0
    if n == 1:
       return 1
    else:
      return fib(n-1) + fib(n-2)



term = fib(17)
print(term)
