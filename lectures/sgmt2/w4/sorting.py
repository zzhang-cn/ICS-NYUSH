from copy import deepcopy

import time
import random
import matplotlib.pyplot as plt


# Global variable that controls max size of the lists
LIMIT = 500

# Optimized bubble sort function
def bubble_sort(my_list):
    N = len(my_list)
    for i in range(1,N):
        swapped = False
        for j in range(0,N-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True
        if swapped == False:
            break
    return my_list


# Merge sort definition
def merge_sort(m):

    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# Merge function definition
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison
        # to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])

    return result


# Function runtime timer
def check_func_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def main():
    randomized_lists_merge = []
    randomized_lists_bubble = []

    print("Generating randomized lists for sorting...")
    for i in range(LIMIT):
        randomized_lists_merge.append( [random.randint(0, j+1) for j in range(i+1)] )
    randomized_lists_bubble = deepcopy(randomized_lists_merge)

    print("Benchmarking merge and bubble sorts...")
    merge_sort_runtimes = []
    bubble_sort_runtimes = []
    for i in range( len(randomized_lists_merge) ):
        print("sorting at size: ", i, ".....")
        merge_sort_runtimes.append(check_func_time(merge_sort,randomized_lists_merge[i]))
        bubble_sort_runtimes.append(check_func_time(bubble_sort,randomized_lists_bubble[i]))

    print("Plotting runtime graphs...")
    plt.plot(merge_sort_runtimes, label='merge sort')
    plt.plot(bubble_sort_runtimes, label='bubble sort')
    plt.xlabel('size')
    plt.ylabel('time')
    plt.legend(loc='upper left')

main()
