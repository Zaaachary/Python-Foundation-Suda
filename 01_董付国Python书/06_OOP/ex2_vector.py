"""
设计一个三维向量，并实现向量的加法、减法以及向量与标量的乘法和除法运算
运算符重载
"""
import random

class Vector3:
    def __init__(self, shape=(1,1,1)):
        if isinstance(shape, tuple) and len(shape) == 3:
            self.shape = shape
            self.creatMat()
        else:
            print('must be a tuple of 3 integer.')
            return 

    def creatMat(self):
        mat = [[] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            mat[i] = [[] for _ in range(self.shape[1])]
            for j in range(self.shape[1]):
                mat[i][j] = [random.randint(0,100) for _ in range(self.shape[2])]
        self.mat = mat

    def setValue(self, i, j, k, v):
        self.mat[i][j][k] = v

    def __str__(self):
        return str(self.mat)

    def __add__(self, v2):
        if self.shape != v2.shape:
            print('not in the same shape')
            return None
        else:
            v3 = Vector3(shape=self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    for k in range(self.shape[2]):
                        v3.setValue(i,j,k, self.mat[i][j][k]+v2.mat[i][j][k])
            return v3

if __name__ == "__main__":
    V1 = Vector3((2,2,2))
    V2 = Vector3((2,2,2))
    print(V1, V2)
    V3 = V1 + V2
    print(V3)