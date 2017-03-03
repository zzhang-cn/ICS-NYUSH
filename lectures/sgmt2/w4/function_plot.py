# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:44:30 2016

@author: Mebius
"""

import matplotlib.pyplot as plt
import math

LIMIT = 15

#linear function
def linear(x):
    return x

#quadratic function
def quad(x):
# change: return a quadratic function
    return x

#cubical function
def cube(x):
# change: return a cubical function
    return x

#log function
def logn(x):
# change: return a log(n) function
    return x

#n*log(n)
def n_logn(x):
# change: return a n*log(n) function
    return x

#exponential function
def exp_2(x):
# change: return a exponential function
    return x

# replace the following line, my_range is a list from 1 to LIMIT integers
my_range = list(range(1,LIMIT))

a = [linear(x) for x in my_range]
b = [quad(x) for x in my_range]
c = [cube(x) for x in my_range]
d = [logn(x) for x in my_range]
e = [n_logn(x) for x in my_range]
f = [exp_2(x) for x in my_range]

# add labels to all the curves
plt.plot(a, 'r-', label = 'linear') # liearn function is red
plt.plot(b, 'g-') # quadratic function is green
plt.plot(c, 'b-') # cubical function is blue
plt.plot(d, 'c-') # log(n) is cyan
plt.plot(e, 'y-') # n*log(n) is yellow
plt.plot(f, 'm-') # expoential function of 2 is magenta
# uncomment below to see the behavior when x is small
#plt.xlim(0, 4); plt.ylim(0, 10)
plt.legend(loc='upper left')
