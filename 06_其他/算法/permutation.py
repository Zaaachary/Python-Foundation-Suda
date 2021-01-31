#! -*- encoding:utf-8 -*-
"""
@File    :   permutation.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   Recursion 就地生成 n 个元素的全排列
"""

def permute(A:list, n:int):
    if n == 0:
        print(A)
    else:
        permute(A, n-1)
        for i in range(n-1, -1, -1):
            A[i], A[n] = A[n], A[i]
            permute(A, n-1)
            A[i], A[n] = A[n], A[i]


if __name__ == "__main__":
    permute([1,2,3], 2)