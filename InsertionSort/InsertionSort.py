import numpy as np

def mySort(list):
    for j in range(1,len(list)):
        key = list[j]
        i = j - 1
        while(i >= 0) and (list[i] > key):
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = key
    return list

#test
mylist = np.random.random(size=10)
print(mylist)
print(mySort(mylist))
