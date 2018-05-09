import random

def randomizedSelect(A,p,r,i):
    if(p==r):
        return A[p]
    q = randomPartition(A,p,r)
    k = q - p + 1
    if(i==k):
        return A[q]
    elif(i < k):
        return randomizedSelect(A,p,q-1,i)
    else:
        return randomizedSelect(A,q+1,r,i-k)

def randomPartition(list, p, r):
    ra = random.randint(p, r)
    list[ra], list[r] = list[r], list[ra]
    x = list[r]
    i = p - 1
    for j in range(p, r):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[r] = list[r], list[i + 1]
    return i + 1

list = [1,3,5,6,9,2,4,6,8,0]
print(randomizedSelect(list,0,9,3))
