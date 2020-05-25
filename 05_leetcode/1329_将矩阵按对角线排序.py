"""
给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。
输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from typing import List
import itertools
import collections

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # 212ms 21%
        m, n = len(mat), len(mat[0])
        temp_list = []
        for line in range(m+n-1):
            # 共m+n-1条对角线
            i, j = m-1-line, 0
            temp_list.clear()
            while j < n:
                # 将对角线上的元素添加到list
                if 0<=i<m and 0<=j<n:
                    temp_list.append(mat[i][j])
                i += 1
                j += 1
            temp_list.sort()
            # 排序后重新写回mat
            i, j = m-1-line, 0
            while j < n:
                if 0<=i<m and 0<=j<n:
                    mat[i][j] = temp_list.pop(0)
                i += 1
                j += 1
        return mat

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, d = len(mat), len(mat[0]), collections.defaultdict(list)
        for i, j in itertools.product(range(m), range(n)):
            d[i - j].append(mat[i][j])
        d = {k: iter(sorted(v)) for k, v in d.items()}
        for i, j in itertools.product(range(m), range(n)):
            mat[i][j] = next(d[i - j])
        return mat


if __name__ == "__main__":
    S = Solution()
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    print(S.diagonalSort(mat))