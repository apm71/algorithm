class heap(object):
    heapsize = 9 #this var must be equals the length-1 of the array

    def heapsort(self, a):
        len = s.heapsize
        s.buildMaxHeap(a)
        for i in range(len, 1, -1):
            #print("%d" % a[1], end=" ")
            a[i],a[1] = a[1],a[i]
            s.heapsize -= 1
            s.maxHeapify(a, 1)
        #print("%d\n" % a[1])

    def buildMaxHeap(self, a):
        for i in range(s.heapsize // 2, 0, -1):
            s.maxHeapify(a, i)

    def maxHeapify(self, a, i):
        left = i << 1
        right = left + 1
        largest = i
        if i <= s.heapsize // 2:
            if left <= s.heapsize and a[left] > a[i]:
                largest = left
            if right <= s.heapsize and a[right] > a[largest]:
                largest = right
            if largest != i:
                a[i],a[largest] = a[largest],a[i]
                s.maxHeapify(a, largest)

if __name__ == "__main__":
    array = [0,4,2,1,3,5,9,8,7,6]
    s = heap()
    s.heapsort(array)
    print(array)
