"""
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

e.g.
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
"""
from typing import List
from math import log

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # 44ms 60%
        ans = set()
        i_max = int(log(bound, x)) if x != 1 else 1
        j_max = int(log(bound, y)) if y != 1 else 1
        for i in range(0, i_max+1):
            for j in range(0, j_max+1):
                interger = x**i + y**j
                if interger <= bound:
                    ans.add(interger)
        return list(ans)

    def powerfulIntegers2(self, x, y, bound):
        # 68ms 18%
        ans = set()
        # 2**20 > bound   bound <= 10 ** 6
        for i in range(20):
            for j in range(20):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)


if __name__ == "__main__":
    S = Solution()
    x, y, bound = 3, 5 ,15
    print(S.powerfulIntegers(x, y, bound))