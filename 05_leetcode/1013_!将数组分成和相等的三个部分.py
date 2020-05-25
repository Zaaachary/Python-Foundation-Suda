"""
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

输入：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

"""
from typing import List
from itertools import product

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 超时
        if len(A) <3:
            return False
        s = 0
        A_sum = []
        for num in A:
            s += num
            A_sum.append(s)
        # 此时s是所有部分的值
        for i in range(0, len(A)-2):
            for j in range(i+1, len(A)-1):
                if A_sum[i] == A_sum[j] - A_sum[i] == s - A_sum[j]:
                    return True

        return False 

    def canThreePartsEqualSum2(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False



if __name__ == "__main__":
    S = Solution()
    print(S.canThreePartsEqualSum([14,6,-10,2,18,-7,-4,11]))   # false
    print(S.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))