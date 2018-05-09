def countingSort(A,k):
    n = len(A)
    B = createList(n - 1)
    C = createList(k)
    for j in range(n):
        C[A[j]] += 1
    for i in range(k):
        C[i] += C[i - 1]
    for j in range(n - 1,-1,-1):
        B[C[A[j]]-2] = A[j]
        C[A[j]] -= 1
    return B

def createList(k):
    list = [0]
    for i in range(k):
        list.append(0)
    return list

#test
A = [5,4,3,2,1,0]
B = countingSort(A,len(A) - 1)
print(B)