import random

def randomQuickSort(list,p,r):
    if p < r:
        q = randomPartition(list, p, r)
        randomQuickSort(list, p, q - 1)
        randomQuickSort(list, q + 1, r)

def randomPartition(list,p,r):
    ra = random.randint(p,r)
    list[ra],list[r] = list[r],list[ra]
    x = list[r]
    i = p - 1
    for j in range(p, r):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[r] = list[r], list[i + 1]
    return i + 1

list = [9,8,7,6,5,4,3,2,1]
randomQuickSort(list,0,len(list) - 1)
print(list)

