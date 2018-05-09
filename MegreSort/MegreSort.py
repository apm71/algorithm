import numpy as np
import math

def myMegreSort(list,p,r):
    if(p < r):
        q = int(math.floor((p+r)/2))
        myMegreSort(list,p,q)
        myMegreSort(list,q+1,r)
        myMegreSortSub(list,p,q,r)
    return list

def myMegreSortSub(list,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    i = j = k = 0
    left = [None] * (n1 + 1)
    right = [None] * (n2 + 1)
    for i in range(n1):
        left[i] = list[p + i - 1]
    for j in range(n2):
        right[j] = list[q + j]
    left[n1] = float('inf')
    right[n2] = float('inf')
    i = j = 0
    for k in range (p - 1,r):
        if(left[i] <= right[j]):
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
    return list

#test
mylist = np.random.random(size=10)
print(mylist)
print(myMegreSort(mylist,1,10))
