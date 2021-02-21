#! -*- encoding:utf-8 -*-
"""
@File    :   Offer 44.数字序列中某一位的数字.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   迭代 + 求整 / 求余

https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 40ms 64.14%
        # 10x1, 90x2, 900x3, 9000x4, 90000x5
        level, size = 10, 1

        while n >= level*size:
            n -= level*size
            size += 1
            level = 9 * 10 ** (size-1)
        else:
            d, m = divmod(n, size)
            temp = 10 ** (size-1) + d if size > 1 else d
            return int(str(temp)[m])




if __name__ == "__main__":
    S = Solution()
    # test = [0, 5, 10, 13, 19]   # 0, 5, 1, 1, 4
    # test = [0, 5, 10, 13, 19]   # 0, 5, 1, 1, 4
    # print([S.findNthDigit(i) for i in range(0,30)])
    # print([S.findNthDigit(i) for i in range(10,30)])
    # print([S.findNthDigit(i) for i in range(80,120)])
    print([S.findNthDigit(i) for i in range(150, 230)])
    # print(S.findNthDigit(100))