# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:46:06 2015

@author: zhengzhang
"""
import time
import matplotlib.pyplot as plt

# timing the execution of a function
def timeit(f, *args):
    t1 = time.time()
    f(*args)
    t2 = time.time()
    return t2 - t1


from copy import deepcopy
def powerset_add(l):
    pset = [[]]
    for item in l:
# note the use of deepcopy, list is mutable!
        new_subset = deepcopy(pset)
# implement logic to add new subset
# for each existing list, add the item, then you need to
# extend pset with new_subsets
        pass
# your code ends here
    return pset
    
# play with the code below in the console, e.g get_bin_str(3, 5)
def get_bin_str(n, up_to):
    code = bin(n).split('b')[-1]
    if len(code) > up_to:
        raise ValueError('not enough')
    code = '0' * (up_to - len(code)) + code
    return code
    
def powerset_comb(l):
    pset = []
    total_items = len(l)
    for i in range(2 ** total_items):
        is_in = get_bin_str(i, total_items)
        subset = []
# implement logic to insert into the subset below
# if is_in[i] is '1', then i-th item is in it
        pass
# your code ends here
        pset.append(subset)
    return pset
    
def main():
    
    num_items = 4
    my_list = list(range(num_items))
    
# test using inductive logic
    my_pset = powerset_add(my_list)
    print("using induction:\n", my_pset)
    
# test using combinational logic
    my_pset = powerset_comb(my_list)
    print("using combination:\n", my_pset)

    exec_time = []

    for i in range(14):
        my_list = list(range(i + 1))
        takes = timeit(powerset_comb, my_list)
        exec_time.append(takes)

    print("powerset", exec_time)    
# once you are done with powerset function, uncomment the line below
# and plot the execution time
    plt.plot(exec_time)

main()