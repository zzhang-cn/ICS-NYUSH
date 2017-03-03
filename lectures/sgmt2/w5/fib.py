import matplotlib.pyplot as plt
import math
import time

#you can define the limit of n here
LIMIT=25

def fast_fib(n, memo={}):
    # replace the following line with a recursion with dynamic programming
    return fib(n)


def fib(n):
    #assume n is a non-negative integer, and the function returns Fib of n
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def check_func_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time
    
my_range = list(range(1,LIMIT))
a = [check_func_time(fib,number) for number in my_range]

plt.plot(my_range,a, 'r-', label = 'Fib') 
plt.legend()
