def mySquareMatrixMultiply(matrixA,matrixB):
    n = len(matrixA)
    m = len(matrixB)
    matrixC = [[0]*n]*m
    i = j = k = 0
    for i in range(n):
        for j in range(n):
            matrixC[i][j] = 0
            for k in range(n):
                matrixC[i][j] += matrixA[i][j]*matrixB[j][k]
    return matrixC
#test
matrixA = matrixB = [[1,1],[1,1]]
matrixB = [[1,2],[3,4]]
print(mySquareMatrixMultiply(matrixA,matrixB))

