import math

def strassen(matrixA,matrixB):
    n = len(matrixA[0])
    halfLen = int(math.floor(n/2))
    matrixC = createMatrix(n)
    if n==1:
        matrixC[0][0] = matrixA[0][0] * matrixB[0][0]
    else:
        a00 = createMatrix(halfLen)
        a01 = createMatrix(halfLen)
        a10 = createMatrix(halfLen)
        a11 = createMatrix(halfLen)
        b00 = createMatrix(halfLen)
        b01 = createMatrix(halfLen)
        b10 = createMatrix(halfLen)
        b11 = createMatrix(halfLen)
        c00 = createMatrix(halfLen)
        c01 = createMatrix(halfLen)
        c10 = createMatrix(halfLen)
        c11 = createMatrix(halfLen)

        copyMatrix(matrixA,a00,0,0)
        copyMatrix(matrixA,a01,0,halfLen)
        copyMatrix(matrixA,a10,halfLen,0)
        copyMatrix(matrixA,a11,halfLen,halfLen)
        copyMatrix(matrixB,b00,0,0)
        copyMatrix(matrixB,b01,0,halfLen)
        copyMatrix(matrixB,b10,halfLen,0)
        copyMatrix(matrixB,b11,halfLen,halfLen)

        matrixadd(strassen(a00,b00),strassen(a01,b10),c00)
        matrixadd(strassen(a00,b01),strassen(a01,b11),c01)
        matrixadd(strassen(a10,b00),strassen(a11,b10),c10)
        matrixadd(strassen(a10,b01),strassen(a11,b11),c11)

        s1 = createMatrix(halfLen)
        s2 = createMatrix(halfLen)
        s3 = createMatrix(halfLen)
        s4 = createMatrix(halfLen)
        s5 = createMatrix(halfLen)
        s6 = createMatrix(halfLen)
        s7 = createMatrix(halfLen)
        s8 = createMatrix(halfLen)
        s9 = createMatrix(halfLen)
        s10 = createMatrix(halfLen)

        matrixsub(b01,b11,s1)
        matrixadd(a00,a01,s2)
        matrixadd(a10,a11,s3)
        matrixsub(b10,b00,s4)
        matrixadd(a00,a11,s5)
        matrixadd(b00,b11,s6)
        matrixsub(a01,a11,s7)
        matrixadd(b10,b11,s8)
        matrixsub(a00,a10,s9)
        matrixadd(b00,b01,s10)

        p1 = strassen(a00,s1)
        p2 = strassen(s2,b11)
        p3 = strassen(s3,b00)
        p4 = strassen(a11,s4)
        p5 = strassen(s5,s6)
        p6 = strassen(s7,s8)
        p7 = strassen(s9,s10)

        temp = createMatrix(halfLen)

        matrixadd(p5,p4,temp)
        matrixsub(temp,p2,temp)
        matrixadd(temp,p6,c00)
        matrixadd(p1,p2,c01)
        matrixadd(p3,p4,c10)
        matrixadd(p5,p1,temp)
        matrixsub(temp,p3,temp)
        matrixsub(temp,p7,c11)

        mixMatrix(c00,matrixC,0,0)
        mixMatrix(c01,matrixC,0,halfLen)
        mixMatrix(c10,matrixC,halfLen,0)
        mixMatrix(c11,matrixC,halfLen,halfLen)
    return matrixC

def createMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix

def matrixadd(matrixA,matrixB,matrixC):
    if matrixA != None and matrixB != None:
        n = len(matrixC)
        for i in range(n):
            for j in range(n):
                matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

def matrixsub(matrixA,matrixB,matrixC):
    if matrixA != None and matrixB != None:
        n = len(matrixC)
        for i in range(n):
            for j in range(n):
                matrixC[i][j] = matrixA[i][j] - matrixB[i][j]

def copyMatrix(matrixSrc,matrixNew,iStart,jStart):
    n = len(matrixNew)
    for i in range(iStart,iStart + n):
        for j in range(jStart,jStart + n):
            matrixNew[i - iStart][j - jStart] = matrixSrc[i][j]

def mixMatrix(matrixSub,matrixC,iStrat,jStrat):
    n = len(matrixSub)
    for i in range(n):
        for j in range(n):
            matrixC[i + iStrat][j + jStrat] = matrixSub[i][j]

#test
matrix01 = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
matrix02 = [[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4],[5,6,7,8,1,2,3,4]]
matrix03 = strassen(matrix01,matrix02)
print(matrix03)
'''
不能定义为[0,0]*n*n的形式 ，不然python会将同一个地址对象*n，导致循环上的错误。
也不能用连续等于的方式赋值。
必须用矩阵创建的封装方法一一创建
'''
