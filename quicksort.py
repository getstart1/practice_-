import random
import sys

sys.setrecursionlimit(1000000000)

def getrandata(num):
    a = []
    i = 0
    while (i < num):
        a.append(random.randint(0, 100))
        i = i+1
    return a


def quicksort(num_list):
    length = len(num_list)
    if (length <= 1):
        return num_list
    breakpoint = random.randint(0, length-1)
    break_num = num_list[breakpoint]
    left = []
    right = []
    for i in range(0, length):
        if (num_list[i] <= break_num):
            left.append(num_list[i])
        else:
            right.append(num_list[i])

    return quicksort(left)+ quicksort(right)



print('ha')
a = getrandata(10)
print(a)
result = quicksort(a)
print(result)
