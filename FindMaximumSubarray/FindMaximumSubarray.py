import math

def myFindMaximumSubarray(list,low,high):
    left = right = cross = [0,0,0]
    leftsum = rightsum = crossum = 0
    if(low==high):
        return(low,high,list[low])
    else:
        mid = math.floor((low + high)/2)
        left = myFindMaximumSubarray(list,low,mid)
        right = myFindMaximumSubarray(list,mid + 1,high)
        cross = findMaxCrossingSubarray(list,low,mid,high)
        if(left[0] > right[0]) and (left[0] > cross[0]):
            return left
        elif(right[0] > left[0]) and (right[0] > cross[0]):
            return right
        else:
            return cross
    return

def findMaxCrossingSubarray(list,low,mid,high):
    leftsum = rightsum = -99999999999999999
    maxleft = maxright = sum = 0
    i = mid
    j = mid + 1
    while(i >= low):
        sum = sum + list[i]
        if(sum > leftsum):
            leftsum = sum
            maxleft = i
        i = i - 1
    sum = 0
    while (j <= high):
        sum = sum + list[j]
        if(sum > rightsum):
            rightsum = sum
            maxright = j
        j = j + 1
    return (leftsum + rightsum,maxleft,maxright)

#test
list = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(myFindMaximumSubarray(list,0,len(list)-1))

