import math
class heap(object):
    heapsize = 4

    def maxHeapify(self,a,i):
        heapsize = heap.heapsize
        largest = i
        left = 2 * i + 1#(i << 1) + 1
        right = left + 1

        if left < s.heapsize and a[left] > a[i]:
            largest = left
        if right < s.heapsize and a[right] > a[largest]:
            largest = right
        if (largest != i):
            a[i],a[largest] = a[largest],a[i]
            s.maxHeapify(a,largest)#这里不要写成myMaxHeap(i)

    def buildMaxHeap(self,a):
        for i in range(s.heapsize // 2, 0, -1):
            s.maxHeapify(a, i)

    def heapSort(self,a):
        len = s.heapsize
        s.buildMaxHeap(a)
        for i in range(len, 0, -1):
            # print("%d" % a[1], end=" ")
            a[i], a[0] = a[0], a[i]
            s.heapsize -= 1
            s.maxHeapify(a, 0)

if __name__ == "__main__":
    array = [0, 4, 2, 1, 3]
    s = heap()
    s.heapsort(array)
    print(array)
