#! -*- encoding:utf-8 -*-
"""
@File    :   70.爬楼梯.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   Leetcode
"""
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        思路：f(n) = f(n-1) + f(n-2)
        结果：36ms; 84.34%; 7.25%
        '''
        if n <= 2:
            return n

        n_1, n_2 = 1, 2
        for _ in range(3, n+1):
            n_1, n_2 = n_2, n_1 + n_2
        return n_2

# @lc code=end

if __name__ == "__main__":
    S = Solution()
    print(S.climbStairs(4))