def quickSort(list,p,r):
    if p < r :
        q = partition(list,p,r)
        quickSort(list, p, q - 1)
        quickSort(list,q + 1,r)

def partition(list,p,r):
    x = list[r]
    i = p - 1
    for j in range(p,r):
        if list[j] <= x:
            i += 1
            list[i],list[j] = list[j],list[i]
    list[i + 1],list[r] = list[r],list[i + 1]
    return i + 1

list = [8,5,0,9,6,4,7,3,2,1]
quickSort(list,0,len(list) - 1)
print(list)